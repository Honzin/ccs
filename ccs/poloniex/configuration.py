# -*- coding: utf8 -*-

"""
This file contains configuration for Poloniex stock.
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


HOSTNAME = "poloniex.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["returnTicker"] = "/public?"
REQUESTS["returnTradeHistory"] = "/public?"
REQUESTS["returnOrderBook"] = "/public?"
REQUESTS["return24hVolume"] = "/public?"
REQUESTS["returnChartData"] = "/public?"
REQUESTS["returnCurrencies"] = "/public?"
REQUESTS["returnLoanOrders"] = "/public?"

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

MAPPING[constants.TICKER] = {constants.LOW: "low24hr",
                             constants.HIGH: "high24hr",
                             constants.ASK: "lowestAsk",
                             constants.BID: "highestBid",
                             constants.LAST: "last",
                             constants.VOLUME24H: "baseVolume"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TID: "globalTradeID",
                            constants.PRICE: "rate",
                            constants.AMOUNT: "amount",
                            constants.TIMESTAMP: "date",
                            constants.TYPE: "type"}

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
        ".+_.+": {
            "type": "object",
            "properties": {
                "id":               {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                "last":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "lowestAsk":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "highestBid":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "percentChange":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "baseVolume":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "quoteVolume":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "isFrozen":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "high24hr":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "low24hr":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["id", "last", "lowestAsk", "highestBid", "percentChange", "baseVolume", "quoteVolume", "isFrozen", "high24hr", "low24hr"]
        }
    }
}

SCHEMA["returnTicker"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADES #########################################################################

DATETIME_PATTERN = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

SCHEMA[constants.UNIFICATED_TRADE] = {
        "type": "object",
        "properties": {
            "globalTradeID": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
            "tradeID":       {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
            "rate":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "amount":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "total":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "type":          {"type": "string", "enum": ["sell", "buy"]},
            "date":          {"type": "string", "pattern": DATETIME_PATTERN},
        },
        "required": ["globalTradeID", "tradeID", "rate", "amount", "type", "date", "total"]
    }

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["returnTradeHistory"] = SCHEMA[constants.UNIFICATED_TRADES]

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
        "asks":         SCHEMA[constants.UNIFICATED_ORDERS],
        "bids":         SCHEMA[constants.UNIFICATED_ORDERS],
        "isFrozen":     {"type": "string"},
        "seq":          {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["asks", "bids", "isFrozen", "seq"],
    "additionalProperties": False
}

SCHEMA["returnOrderBook"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]

# 24H VOLUME #######################################################################

SCHEMA["return24hVolume"] = {
    "type": "object",
    "properties": {
        ".+_.+": {
            "type": "object",
            "properties": {
                ".+":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
        },
        "total.+":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "minProperties": 2,
}

# CHARTA DATA #######################################################################

SCHEMA["returnChartData"] = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "date":               {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
            "high":               {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "low":                {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "open":               {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "close":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "volume":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "quoteVolume":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "weightedAverage":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
        },
        "required": ["date", "high", "low", "open", "close", "volume", "quoteVolume", "weightedAverage"]
    }
}

# CURRENCIES #######################################################################

SCHEMA["returnCurrencies"] = {
    "type": "object",
    "properties": {
        ".+": {
            "type": "object",
            "properties": {
                "id":               {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                "name":             {"type": "string"},
                "txFee":            {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "minConf":          {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                "depositAddress":   {},
                "disabled":         {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                "delisted":         {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                "frozen":           {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["id", "name", "txFee", "minConf", "depositAddress", "disabled", "delisted", "frozen"]
        }
    },
    "minProperties": 2,
}

# LOAN ORDERS #######################################################################

# TODO  REMOVE DUPLICITY

SCHEMA["returnLoanOrders"] = {
    "type": "object",
    "properties": {
        "offers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "rate":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "amount":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "rangeMin": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                    "rangeMax": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN}
                },
                "required": ["rate", "amount", "rangeMin", "rangeMax"]
            }
        },
        "demands": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "rate":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "amount":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "rangeMin": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
                    "rangeMax": {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN}
                },
                "required": ["rate", "amount", "rangeMin", "rangeMax"]
            }
        }
    },
    "required": ["offers", "demands"]
}
