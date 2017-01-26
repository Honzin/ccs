# -*- coding: utf8 -*-

"""
This file contains configuration for Bitfinex stock.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"


from .. import constants
from .. import default

##################################################################################
# HOSTNAME                                                                       #
##################################################################################

HOSTNAME = "api.bitfinex.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/v1/pubticker/[symbol]"
REQUESTS["trades"] = "/v1/trades/[symbol]/?"
REQUESTS["orderbook"] = "/v1/book/[symbol]/?"
REQUESTS["symbols"] = "/v1/symbols/"
REQUESTS["stats"] = "/v1/stats/[symbol]"
REQUESTS["fundingbook"] = "/v1/lendbook/[currency]?"
REQUESTS["lends"] = "/v1/lends/[currency]?"
REQUESTS["symbolsDetails"] = "/v1/symbols_details"


##################################################################################
# HEADERS                                                                        #
##################################################################################

HEADER = default.HEADER
COMPRESSION = constants.GZIP
TIMEOUT = default.TIMEOUT

##################################################################################
# MAPPING                                                                        #
##################################################################################

MAPPING = {}

# TICKER #########################################################################

MAPPING[constants.TICKER] = {constants.LAST: "last_price",
                             constants.VOLUME24H: "volume"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TYPE: "type"}
default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "buy", constants.SELL: "sell"}

# ORDERBOOK #######################################################################

MAPPING[constants.ORDER] = {}
default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

# TICKER #########################################################################

SCHEMA[constants.UNIFICATED_TICKER] = {
  "type": "object",
  "properties": {
    "mid":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "bid":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "ask":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "last_price": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "low":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "high":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "volume":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    "timestamp":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
  },
  "required": ["mid", "bid", "ask", "last_price", "low", "high", "volume", "timestamp"]
}

SCHEMA["ticker"] = SCHEMA[constants.UNIFICATED_TICKER]


# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
        "type": "object",
        "properties": {
            "tid":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "amount":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "type":         {"type": "string", "enum": ["sell", "buy"]},
            "exchange":     {"type": "string"},
            "timestamp":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
        },
        "required": ["tid", "price", "amount", "type", "exchange","timestamp"],
    }

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["trades"] = SCHEMA[constants.UNIFICATED_TRADES]

# ORDERBOOK #######################################################################

SCHEMA[constants.UNIFICATED_ORDER] = {
    "type": "object",
    "properties": {
        "price":     {"type": "string", "pattern": constants.NUMBER_PATTERN},
        "amount":    {"type": "string", "pattern": constants.NUMBER_PATTERN},
        "timestamp": {"type": "string", "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["price", "amount", "timestamp"],
}

SCHEMA[constants.UNIFICATED_ORDERS] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_ORDER]
}

SCHEMA[constants.UNIFICATED_ORDERBOOK] = {
    "type": "object",
    "properties": {
        "asks": SCHEMA[constants.UNIFICATED_ORDERS],
        "bids": SCHEMA[constants.UNIFICATED_ORDERS]
    },
    "required": ["asks", "bids"],
}


SCHEMA["orderbook"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# SYMBOLS #######################################################################

SCHEMA["symbols"] = {
  "type": "array",
  "items": {"type": "string"}
}

# STATS #######################################################################

SCHEMA["stats"] = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "period": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
      "volume": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    },
    "required": ["period", "volume"]
  }
}

# FUNDINGBOOK #######################################################################

SCHEMA["fundingbook_item"] = {
        "type": "object",
        "properties": {
          "rate":       {"type": "string"},
          "amount":     {"type": "string"},
          "period":     {"type": "integer"},
          "timestamp":  {"type": "string"},
          "frr":        {"type": "string"}
        },
        "required": ["rate", "amount", "period", "timestamp", "frr"]
      }

SCHEMA["fundingbook"] = {
  "type": "object",
  "properties": {
    "bids": {
      "type": "array",
      "items": SCHEMA["fundingbook_item"],
    },
    "asks": {
      "type": "array",
      "items": SCHEMA["fundingbook_item"],
    }
  },
  "required": ["bids", "asks"]
}

# LENDS #######################################################################

SCHEMA["lends"] = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "rate":           {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
      "amount_lent":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "amount_used":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "timestamp":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["rate", "amount_lent", "amount_used", "timestamp"]
  }
}

# SYMBOLS DETAILS #######################################################################

SCHEMA["symbolsDetails"] = {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "pair":                   {"type": "string"},
      "price_precision":        {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
      "initial_margin":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "minimum_margin":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "maximum_order_size":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "minimum_order_size":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
      "expiration":             {"type": "string"}
    },
    "required": ["pair", "price_precision", "initial_margin", "minimum_margin", "maximum_order_size", "minimum_order_size", "expiration"]
  }
}

