# -*- coding: utf8 -*-

"""
This file contains configuration for Okcoin.cn stock.
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

from ..okcoin.configuration import *

##################################################################################
# HOSTNAME                                                                       #
##################################################################################


HOSTNAME = "www.okcoin.cn"

##################################################################################
# REQUEST                                                                        #
##################################################################################

# REQUESTS = {}
# REQUESTS["ticker"] = "/api/v1/ticker.do?"
# REQUESTS["trades"] = "/api/v1/trades.do?"
# REQUESTS["depth"] = "/api/v1/depth.do?"
# REQUESTS["kline"] = "/api/v1/kline.do"

##################################################################################
# HEADERS                                                                        #
##################################################################################

# HEADER = default.HEADER
# COMPRESSION = constants.IDENTITY
# TIMEOUT = default.TIMEOUT

##################################################################################
# MAPPING                                                                        #
##################################################################################

# MAPPING = {}

# TICKER #########################################################################

# DEFAULT
# TICKER = {LOW: 'low',
#           HIGH: 'high',
#           ASK: 'ask',
#           BID: 'bid',
#           LAST: 'last',
#           VOLUME24H: 'volume24h',
#           TIMESTAMP: 'timestamp'}

# MAPPING[constants.TICKER] = {}
# default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

# DEFAULT
# TRADE = {TID: "tid",
#          PRICE: "price",
#          AMOUNT: "amount",
#          TIMESTAMP: "timestamp"}

# MAPPING[constants.TRADE] = {}
# default.complete(default.TRADE, MAPPING[constants.TRADE])
#
# MAPPING[constants.TRADE_TYPE] = "" #{constants.BUY: "buy", constants.SELL: "sell"}

# ORDERBOOK #######################################################################

# DEFAULT
# ORDER = {PRICE: "price", AMOUNT: "amount"}

# MAPPING[constants.ORDER] = {}
# default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

# SCHEMA = {}

# TICKER #########################################################################

# {
#   "type": "object",
#   "properties": {
#     "mid":        {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "bid":        {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "ask":        {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "last_price": {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "low":        {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "high":       {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "volume":     {"type": "string", "pattern": constants.NUMBER_PATTERN},
#     "timestamp":  {"type": "string", "pattern": constants.NUMBER_PATTERN}
#   },
#   "minProperties": 8,
#   "additionalProperties": False
#
# }
# SCHEMA[constants.TICKER] = {}

# TRADES #########################################################################

# {
#         "type": "object",
#         "properties": {
#             "tid": {"type": "number"},
#             "price": {"type": "string", "pattern": constants.NUMBER_PATTERN},
#             "amount": {"type": "string", "pattern": constants.NUMBER_PATTERN},
#             "type": {"type": "string", "enum": ["sell", "buy"]},
#             "exchange": {"type": "string"},
#             "timestamp": {"type": "number"}
#         },
#         "required": ["tid", "price", "amount", "type", "exchange","timestamp"],
#         "additionalProperties": False
#     }
# SCHEMA[constants.TRADE] = {}

# {
#     "type": "array",
#     "items": SCHEMA[constants.TRADE]
# }
# SCHEMA[constants.TRADES] = {}


# ORDERBOOK #######################################################################

# {
#     "type": "object",
#     "properties": {
#         "price":     {"type": "string", "pattern": constants.NUMBER_PATTERN},
#         "amount":    {"type": "string", "pattern": constants.NUMBER_PATTERN},
#         "timestamp": {"type": "string", "pattern": constants.NUMBER_PATTERN}
#     },
#     "required": ["price", "amount", "timestamp"],
#     "additionalProperties": False
# }
# SCHEMA[constants.ORDER] = {}


# {
#     "type": "array",
#     "items": SCHEMA[constants.ORDER]
# }
# SCHEMA[constants.ORDERS] = {}


# {
#     "type": "object",
#     "properties": {
#         "asks": SCHEMA[constants.ORDERS],
#         "bids": SCHEMA[constants.ORDERS]
#     },
#     "required": ["asks", "bids"],
#     "additionalProperties": False
# }
# SCHEMA[constants.ORDERBOOK] = {}

