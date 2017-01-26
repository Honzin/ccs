# -*- coding: utf8 -*-

"""
This file contains configuration for Bitstamp stock.
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

HOSTNAME = "www.bitstamp.net"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/api/v2/ticker/[symbol]"
REQUESTS["transactions"] = "/api/v2/transactions/[symbol]/?"
REQUESTS["orderbook"] = "/api/v2/order_book/[symbol]/"
REQUESTS["hourlyTicker"] = "/api/v2/ticker_hour/[symbol]/"
REQUESTS["eurUsdConversionRate"] = "/api/eur_usd/"


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

MAPPING[constants.TICKER] = {constants.VOLUME24H: "volume"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TYPE: "type", constants.TIMESTAMP: "date"}
default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "0", constants.SELL: "1"}

# ORDERBOOK #######################################################################

MAPPING[constants.ORDER] = {constants.PRICE: 0, constants.AMOUNT: 1}
# default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

# TICKER #########################################################################

SCHEMA[constants.UNIFICATED_TICKER] = {
    "type": "object",
    "properties": {
        "open":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "vwap":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "bid":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "ask":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "last":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "low":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "high":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "volume":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "timestamp":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["open", "vwap", "bid", "ask", "last", "low", "high", "volume", "timestamp"]
}

SCHEMA["ticker"]       = SCHEMA[constants.UNIFICATED_TICKER]
SCHEMA["hourlyTicker"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
        "type": "object",
        "properties": {
            "tid":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "price":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "amount": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "type":   {"type": "string", "pattern": constants.NUMBER_PATTERN, "enum": ["0", "1"]},
            "date":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
        },
        "required": ["tid", "price", "amount", "type", "date"]
    }

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["transactions"] = SCHEMA[constants.UNIFICATED_TRADES]

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
        "timestamp":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "asks":       SCHEMA[constants.UNIFICATED_ORDERS],
        "bids":       SCHEMA[constants.UNIFICATED_ORDERS]
    },
    "required": ["asks", "bids", "timestamp"]
}

SCHEMA["orderbook"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# EUR USD CONVERSION RATE #######################################################################

SCHEMA["eurUsdConversionRate"] = {
    "type": "object",
    "properties": {
        "sell": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "buy":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
    },
    "required": ["sell", "buy"]
}