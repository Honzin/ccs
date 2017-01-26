# -*- coding: utf8 -*-

"""
This file contains configuration for Bter stock.
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


HOSTNAME = "data.bter.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/api/1/ticker/[symbol]"
REQUESTS["tradeHistory"] = "/api/1/trade/[symbol]"
REQUESTS["depth"] = "/api/1/depth/[symbol]"
REQUESTS["tradingPairs"] = "/api/1/pairs"
REQUESTS["marketInfo"] = "/api/1/marketinfo"
REQUESTS["marketDetails"] = "/api/1/marketlist"
REQUESTS["tickers"] = "/api/1/tickers"

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

MAPPING[constants.TICKER] = {constants.ASK: "sell",
                             constants.BID: "buy"}

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
        "buy":                    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "sell":                   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "last":                   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "avg":                    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "low":                    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "high":                   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "result":                 {"type": "string"},
        "vol_btc":                {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "vol_cny":                {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "rate_change_percentage": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["result", "last", "high", "low", "avg", "sell", "buy", "vol_btc", "vol_cny", "rate_change_percentage"]
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
    "type": "object",
    "properties": {
        "result": {"type": "string"},
        "data": {
            "type": "array",
            "items": SCHEMA[constants.UNIFICATED_TRADE]
        },
        "elapsed": {"type": "string"}
    },
    "required": ["result", "data", "elapsed"]
}

SCHEMA["tradeHistory"] = SCHEMA[constants.UNIFICATED_TRADES]

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
        "result": {"type": "string"}, # TODO enum true
        "asks": SCHEMA[constants.UNIFICATED_ORDERS],
        "bids": SCHEMA[constants.UNIFICATED_ORDERS]
    },
    "required": ["result", "asks", "bids"]
}

SCHEMA["depth"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# TRAIDING PAIRS #######################################################################

SCHEMA["tradingPairs"] = {
    "type": "array",
    "items": {"type": "string"}
}

# MARKET INFO #######################################################################

SCHEMA["marketInfo"] = {
    "type": "object",
    "properties": {
        "result": {"type": "string"},
        "pairs": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    ".+_.+": {
                        "type": "object",
                        "properties": {
                            "decimal_places":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                            "min_amount":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                            "fee":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                        },
                        "required": ["decimal_places", "min_amount", "fee"]
                    }
                }
            }
        }
    },
    "required": ["result", "pairs"]
}

# MARKET DETAILS #######################################################################

SCHEMA["marketDetails"] = {
    "type": "object",
    "properties": {
        "result": {"type": "string"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "no":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "symbol":       {"type": "string"},
                    "name":         {"type": "string"},
                    "name_cn":      {"type": "string"},
                    "pair":         {"type": "string"},
                    "rate":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "vol_a":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "vol_b":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "curr_a":       {"type": "string"},
                    "curr_b":       {"type": "string"},
                    "curr_suffix":  {"type": "string"},
                    "rate_percent": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "trend":        {"type": "string"},
                    "supply":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "marketcap":    {"type": ["string", "number", "null"]},
                    "plot":         {}
                },
                "required": ["no", "symbol", "name", "name_cn", "pair", "rate", "vol_a", "vol_b", "curr_a", "curr_b", "curr_suffix", "rate_percent", "trend", "supply", "marketcap", "plot"]
            }
        }
    },
    "required": ["result", "data"]
}

# TICKERS #######################################################################

SCHEMA["tickers"] = {
    "type": "object",
    "properties": {
        ".+_.+": {
            "type": "object",
            "properties": {
                "result":                   {"type": "string"},
                "last":                     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "high":                     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "low":                      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "avg":                      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "sell":                     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "buy":                      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "vol_btc":                  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "vol_cny":                  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "rate_change_percentage":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["result", "last", "high", "low", "avg", "sell", "buy", "vol_btc", "vol_cny", "rate_change_percentage"]
        }
    }
}
