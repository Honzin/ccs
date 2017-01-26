# -*- coding: utf8 -*-

"""
This file contains configuration for Btcc-spot stock.
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

import copy

##################################################################################
# HOSTNAME                                                                       #
##################################################################################


HOSTNAME = "data.btcchina.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/data/ticker?"
REQUESTS["trades"] = "/data/trades?"
REQUESTS["orderbook"] = "/data/orderbook?"
REQUESTS["tradeHistory"] = "/data/historydata?"

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
                             constants.TIMESTAMP: "date"}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TIMESTAMP: "date"}

default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {}

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
        "buy":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "sell":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "last":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "vwap":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "low":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "high":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "vol":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "open":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "prev_close":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "date":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["high", "low", "buy", "sell", "last", "vol", "date", "vwap", "prev_close", "open"]
}

SCHEMA["ticker"] = {
    "type": "object",
    "properties": {
        "ticker.*": SCHEMA[constants.UNIFICATED_TICKER],
    }
}

# TRADES #########################################################################

# TODO Solve UNIFICATED_TRADES = "trades" or UNIFICATED_TRADES="tradeHistory"

SCHEMA["trade"] = {
    "type": "object",
    "properties": {
        "tid":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "price":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "amount":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "date":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["tid", "price", "amount", "date"]
}

SCHEMA["trades"] = {
    "type": "array",
    "items": SCHEMA["trade"]
}


# TRADE HISTORY #######################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
    "type": "object",
    "properties": {
        "tid":      {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "price":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "amount":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "date":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "type":     {"type": "string", "enum": ["sell", "buy"]}
    },
    "required": ["tid", "price", "amount", "date", "type"]
}

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["tradeHistory"] = SCHEMA[constants.UNIFICATED_TRADES]

# ORDERBOOK #######################################################################

SCHEMA[constants.ORDER] = {
    "type": "array",
    "items":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
}

SCHEMA[constants.ORDERS] = {
    "type": "array",
    "items": SCHEMA[constants.ORDER]
}

SCHEMA[constants.ORDERBOOK] = {
    "type": "object",
    "properties": {
        "date": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "asks": SCHEMA[constants.ORDERS],
        "bids": SCHEMA[constants.ORDERS]
    },
    "required": ["asks", "bids", "date"]
}

# TODO do deepcopy for all stocks
SCHEMA["orderbook"] = SCHEMA[constants.ORDERBOOK]