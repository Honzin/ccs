# -*- coding: utf8 -*-

"""
This file contains configuration for Cexio stock.
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


HOSTNAME = "cex.io"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/api/ticker/"
REQUESTS["tradeHistory"] = "/api/trade_history/"
REQUESTS["orderbook"] = "/api/order_book/"
REQUESTS["currencyLimits"] = "/api/currency_limits"
REQUESTS["lastPrice"] = "/api/last_price/"
REQUESTS["historical1mOHLCVChart"] = "/api/ohlcv/hd/"
REQUESTS["tickersForAllPairsByMarket"] = "/api/tickers/"
REQUESTS["lastPricesForGivenMarket"] = "/api/last_prices/"
REQUESTS["convert"] = "/api/convert/"
REQUESTS["chart"] = "/api/price_stats/"

##################################################################################
# HEADERS                                                                        #
##################################################################################

HEADER = default.HEADER
COMPRESSION = constants.IDENTITY
TIMEOUT = default.TIMEOUT

##################################################################################
# MAPPING                                                                        #
##################################################################################

MAPPING = {}

# TICKER #########################################################################

MAPPING[constants.TICKER] = {constants.VOLUME24H: "volume"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TIMESTAMP: "date", constants.TYPE: "type"}

default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "buy", constants.SELL: "sell"}

# ORDERBOOK #######################################################################


MAPPING[constants.ORDER] = {constants.PRICE: 0, constants.AMOUNT: 1}
# default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

# TODO
# REMOVE IF COMMENTED
TIMESTAMP_PATTERN = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*?'

# TICKER #########################################################################

SCHEMA[constants.UNIFICATED_TICKER] = {
    "type": "object",
    "properties": {
        "last":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "volume30d": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "low":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "high":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "volume":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "bid":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "ask":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "timestamp": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["timestamp", "low", "high", "last", "volume", "volume30d", "bid", "ask"]
}

SCHEMA["ticker"] = SCHEMA[constants.UNIFICATED_TICKER]


# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
    "type": "object",
    "properties": {
        "tid":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "price":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "amount": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "type":   {"type": "string", "enum": ["buy", "sell"]},
        "date":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["tid", "price", "amount", "date", "type"]
}
SCHEMA[constants.UNIFICATED_TRADES] = {
            "type": "array",
            "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["tradeHistory"] = SCHEMA[constants.UNIFICATED_TRADES]

# ORDERBOOK #######################################################################

SCHEMA[constants.UNIFICATED_ORDER] = {
    "type": "array",
    "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
}

SCHEMA[constants.UNIFICATED_ORDERS] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_ORDER]
}

SCHEMA[constants.UNIFICATED_ORDERBOOK] = {
    "type": "object",
    "properties": {
        "timestamp": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}, # TODO enum true
        "asks": SCHEMA[constants.UNIFICATED_ORDERS],
        "bids": SCHEMA[constants.UNIFICATED_ORDERS],
        "id": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "pair": {"type": "string",  "pattern": ".+:.+"},
        "sell_total":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "buy_total":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["timestamp", "asks", "bids", "id", "pair", "sell_total", "buy_total"]
}

SCHEMA["orderbook"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# CURRENCY LIMITS #######################################################################

SCHEMA["currencyLimits"] = {
    "type": "object",
    "properties": {
        "e":    {"type": "string"},
        "ok":   {"type": "string"},
        "data": {
            "type": "object",
            "properties": {
                "pairs": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "symbol1": {"type": "string"},
                            "symbol2": {"type": "string"},
                            "minLotSize": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                            "minLotSizeS2": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                            "maxLotSize": {},
                            "minPrice": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                            "maxPrice": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                        },
                        "required": ["symbol1", "symbol2", "minLotSize", "minLotSizeS2", "maxLotSize", "minPrice", "maxPrice"]
                    },
                    "minItems": 1
                }
            },
            "required": ["pairs"]
        }
    },
    "required": ["e", "ok", "data"]
}

# TICKERS FOR ALL PAIRS BY MARKET #######################################################################

SCHEMA["tickersForAllPairsByMarket"] = {
    "type": "object",
    "properties": {
        "e":    {"type": "string"},
        "ok":   {"type": "string"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "timestamp":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "pair":         {"type": "string"},
                    "low":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "high":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "last":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "volume":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "volume30d":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "bid":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "ask":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                },
                "required": ["timestamp", "pair", "low", "high", "last", "volume", "volume30d", "bid", "ask"]
            },
            "minItems": 1
        }
    },
    "required": ["e", "ok", "data"]
}

# LAST PRICE #######################################################################

SCHEMA["lastPrice"] = {
    "type": "object",
    "properties": {
        "lprice":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "curr1":    {"type": "string"},
        "curr2":    {"type": "string"}
    },
    "required": ["lprice", "curr1", "curr2"]
}

# LAST PRICES FOR GIVEN MARKET #######################################################################

SCHEMA["lastPricesForGivenMarket"] = {
  "type": "object",
  "properties": {
    "e":    {"type": "string"},
    "ok":   {"type": "string"},
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "symbol1":    {"type": "string"},
          "symbol2":    {"type": "string"},
          "lprice":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
        },
        "required": ["symbol1", "symbol2", "lprice"]
      }
    }
  },
  "required": ["e", "ok", "data"]
}