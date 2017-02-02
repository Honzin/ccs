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


HOSTNAME = "pro-data.btcc.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["ticker"] = "/data/pro/ticker?"
REQUESTS["orderbook"] = "/data/pro/orderbook?"
REQUESTS["tradeHistory"] = "/data/pro/historydata?"

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

MAPPING[constants.TICKER] =   {constants.LOW: 'Low',
                               constants.HIGH: 'High',
                               constants.ASK: 'AskPrice',
                               constants.BID: 'BidPrice',
                               constants.LAST: 'Last',
                               constants.VOLUME24H: 'Volume24H',
                               constants.TIMESTAMP: 'Timestamp'}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TID: "Id",
                            constants.PRICE: "Price",
                            constants.AMOUNT: "Quantity",
                            constants.TYPE: "Side",
                            constants.TIMESTAMP: "Timestamp"}

default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "Buy", constants.SELL: "Sell"}

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
        "ticker.*": {
            "type": "object",
            "properties": {
                "BidPrice":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "AskPrice":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Open":                 {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "High":                 {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Low":                  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Last":                 {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "LastQuantity":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "PrevCls":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Volume":               {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Volume24H":            {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Timestamp":            {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "ExecutionLimitDown":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "ExecutionLimitUp":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["BidPrice", "AskPrice", "Open", "High", "Low", "Last", "LastQuantity", "PrevCls", "Volume", "Volume24H", "Timestamp", "ExecutionLimitDown", "ExecutionLimitUp"]
        }
    }
}

SCHEMA["ticker"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADE HISTORY #######################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
    "type": "object",
    "properties": {
        "Id":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Timestamp":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Quantity":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Side":         {"type": "string", "enum": ["Sell", "Buy"]}
    },
    "required": ["Id", "Timestamp", "Price", "Quantity", "Side"]
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