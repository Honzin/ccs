# -*- coding: utf8 -*-

"""
This file contains configuration for Okcoin stock.
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


# HOSTNAME = "www.okcoin."

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/api/v1/ticker.do?"
REQUESTS["trades"] = "/api/v1/trades.do?"
REQUESTS["depth"] = "/api/v1/depth.do?"
REQUESTS["kline"] = "/api/v1/kline.do"


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

MAPPING[constants.TICKER] = {constants.ASK: "buy",
                             constants.BID: "sell",
                             constants.VOLUME24H: "vol"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TYPE: "type", constants.TIMESTAMP: "date"}
default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "buy", constants.SELL: "sell"}

# ORDERBOOK #######################################################################

MAPPING[constants.ORDER] = {constants.PRICE: 0, constants.AMOUNT: 1}
default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

# TICKER #########################################################################

SCHEMA[constants.UNIFICATED_TICKER] = {
    "type": "object",
    "properties": {
        "date": {"type": "string", "pattern": constants.NUMBER_PATTERN},
        "ticker": {
            "type": "object",
            "properties": {
                "buy":   {"type": "string", "pattern": constants.NUMBER_PATTERN},
                "sell":  {"type": "string", "pattern": constants.NUMBER_PATTERN},
                "last":  {"type": "string", "pattern": constants.NUMBER_PATTERN},
                "low":   {"type": "string", "pattern": constants.NUMBER_PATTERN},
                "high":  {"type": "string", "pattern": constants.NUMBER_PATTERN},
                "vol":   {"type": "string", "pattern": constants.NUMBER_PATTERN},
            },
            "required": ["buy", "high", "last", "low", "sell", "vol"]
        }
    },
    "required": ["date", "ticker"]
}

SCHEMA["ticker"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
        "type": "object",
        "properties": {
            "tid":     {"type": "number"},
            "price":   {"type": "string", "pattern": constants.NUMBER_PATTERN},
            "amount":  {"type": "string", "pattern": constants.NUMBER_PATTERN},
            "type":    {"type": "string", "enum": ["sell", "buy"]},
            "date":    {"type": "number"},
            "date_ms": {"type": "number"}
        },
        "required": ["tid", "price", "amount", "type", "date", "date_ms"]
    }

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["trades"] = SCHEMA[constants.UNIFICATED_TRADES]

# ORDERBOOK #######################################################################

SCHEMA[constants.UNIFICATED_ORDER] = {
    "type": "array",
    "items": {"type": "number"}
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
    "required": ["asks", "bids"]
}

SCHEMA["depth"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]
