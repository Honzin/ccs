# -*- coding: utf8 -*-

"""
This file contains configuration for Btce stock.
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


HOSTNAME = "btc-e.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/api/3/ticker/[symbol]"
REQUESTS["trades"] = "/api/3/trades/[symbol]/?"
REQUESTS["depth"]  = "/api/3/depth/[symbol]/?"
REQUESTS["info"]   = "/api/3/info"

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
                             constants.VOLUME24H: "vol",
                             constants.TIMESTAMP: "updated"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TYPE: "type"}

default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "bid", constants.SELL: "ask"}

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
        ".+_.+": {
            "type": "object",
            "properties": {
                "buy":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "sell":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "last":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "avg":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "low":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "high":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "vol":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "vol_cur":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "update":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["high", "low", "avg", "vol", "vol_cur", "last", "buy", "sell", "updated"]
        }
    }
}

SCHEMA["ticker"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
    "type": "object",
    "properties": {
        "tid":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "amount":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "type":         {"type": "string", "enum": ["bid", "ask"]},
        "timestamp":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["tid", "price", "amount", "timestamp", "type"]
}
SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "object",
    "properties": {
        ".+_.+": {
            "type": "array",
            "items": SCHEMA[constants.UNIFICATED_TRADE]
        }
    },
    "additionalProperties": False,
    "maxProperties": 1,
    "minProperties": 1
}

SCHEMA["trades"] = SCHEMA[constants.UNIFICATED_TRADES]

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
        ".+_.+": {
            "type": "object",
            "properties": {
                "asks": SCHEMA[constants.UNIFICATED_ORDERS],
                "bids": SCHEMA[constants.UNIFICATED_ORDERS]

            },
            "required": ["asks", "bids"]
        }
    }
}

SCHEMA["depth"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# INFO #######################################################################

SCHEMA["info"] = {
    "type": "object",
    "properties": {
        "server_time": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "pairs": {
            "type": "object",
            "properties": {
                ".+_.+": {
                    "type": "object",
                    "properties": {
                        "decimal_places":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                        "min_price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                        "max_price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                        "min_amount":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                        "hidden":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                        "fee":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                    },
                    "required": ["decimal_places", "min_price", "max_price", "min_amount", "hidden", "fee"]
                }
            }
        }
    },
    "required": ["server_time", "pairs"]
}
