# -*- coding: utf8 -*-

"""
This file contains configuration for Kraken stock.
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


HOSTNAME = "api.kraken.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

# TODO
# prejmenovat pouze na ticker ...
# stejne jak jsou sluzby pojmenovane v URL

REQUESTS = {}
REQUESTS["getTickerInformation"] = "/0/public/Ticker?"
REQUESTS["getRecentTrades"] = "/0/public/Trades?"
REQUESTS["getOrderBook"] = "/0/public/Depth?"
REQUESTS["getTradableAssetPairs"] = "/0/public/AssetPairs?"
REQUESTS["getServerTime"] = "/0/public/Time"
REQUESTS["getAssetInfo"] = "/0/public/Assets"
REQUESTS["getOHLCdata"] = "/0/public/OHLC?"
REQUESTS["getRecentSpreadData"] = "/0/public/Spread?"

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

MAPPING[constants.TICKER] = {constants.LOW: 'l',
                             constants.HIGH: 'h',
                             constants.ASK: "a",
                             constants.BID: "b",
                             constants.LAST: "c",
                             constants.VOLUME24H: "v",
                             constants.TIMESTAMP: None}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.PRICE: 0,
                            constants.AMOUNT: 1,
                            constants.TIMESTAMP: 2,
                            constants.TYPE: 3}

#default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "b", constants.SELL: "s"}

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
        "error": {},
        "result": {
            "type": "object",
            "properties": {
                "X.+": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "b": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "c": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "v": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "p": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "t": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "l": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "h": {"type": "array", "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}},
                        "o": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                    },
                    "required": ["a", "b", "c", "v", "p", "t", "l", "h", "o"]
                }
            },
            "minProperties": 1,
            #"additionalProperties": False
        }
    },
    "required": ["error", "result"],
    #"additionalProperties": False
}

SCHEMA["getTickerInformation"] = SCHEMA[constants.UNIFICATED_TICKER]

# TRADES #########################################################################
# TODO string pattern
SCHEMA[constants.UNIFICATED_TRADE] = {
    "type": "array",
    "items": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
}
SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "object",
    "properties": {
        "error": {},
        "result": {
            "type": "object",
            "properties": {
                "last": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "X.+":  {"type": "array", "items": SCHEMA[constants.UNIFICATED_TRADE]}
            },
            "minProperties": 2,
        }
    },
    "required": ["error", "result"]
}

SCHEMA["getRecentTrades"] = SCHEMA[constants.UNIFICATED_TRADES]

# ORDERBOOK #######################################################################
# TODO string pattern
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
        "error": {},
        "result": {
            "type": "object",
            "properties": {
                "X.+": {
                    "type": "object",
                    "properties": {
                        "asks": SCHEMA[constants.UNIFICATED_ORDERS],
                        "bids": SCHEMA[constants.UNIFICATED_ORDERS]
                    },
                    "required": ["asks", "bids"]
                }
            }
        }
    },
    "required": ["error", "result"]
}

SCHEMA["getOrderBook"] = SCHEMA[constants.UNIFICATED_ORDERBOOK]


SCHEMA["getTradableAssetPairs"] = {
    "type": "object",
    "properties": {
        "error": {"type": "array", "items": {}},
        "result": {
            "type": "object",
            "properties": {
                "X.+": {
                    "type": "object",
                    "properties": {
                        "altname": {"type": "string"},
                        "aclass_base": {"type": "string"},
                        "base": {"type": "string"},
                        "aclass_quote": {"type": "string"},
                        "quote": {"type": "string"},
                        "lot": {"type": "string"},
                        "pair_decimals": {"type": "integer"},
                        "lot_decimals": {"type": "integer"},
                        "lot_multiplier": {"type": "integer"},
                        "leverage_buy": {"type": "array", "items": {"type": "integer"}},
                        "leverage_sell": {"type": "array", "items": {"type": "integer"}},
                        "fees":{
                            "type": "array",
                            "items": {"type": "array", "items": {"type": "integer"}}
                        },
                        "fee_volume_currency": {"type": "string"},
                        "margin_call": {"type": "integer"},
                        "margin_stop": {"type": "integer"}
                    },
                    "required": ["altname", "aclass_base", "base", "aclass_quote", "quote", "lot", "pair_decimals", "lot_decimals", "lot_multiplier", "leverage_buy", "leverage_sell", "fees", "fee_volume_currency", "margin_call", "margin_stop"]
                }
            }
        }
    },
    "required": ["error", "result"]
}

SCHEMA["getServerTime"] = {
    "type": "object",
    "properties": {
        "error": {"type": "array", "items": {}},
        "result": {
            "type": "object",
            "properties": {
                "unixtime": {"type": "integer"},
                "rfc1123": {"type": "string"}
            }
        }
    },
    "required": ["error", "result"]
}


SCHEMA["getAssetInfo"] = {
    "type": "object",
    "properties": {
        "error": {"type": "array", "items": {}},
        "result": {
            "type": "object",
            "properties": {
                ".+": {
                    "type": "object",
                    "properties": {
                        "aclass": {"type": "string"},
                        "altname": {"type": "string"},
                        "decimals": {"type": "integer"},
                        "display_decimals": {"type": "integer"}
                    },
                    "required": ["aclass", "altname", "decimals", "display_decimals"]
                },
            }
        }
    },
    "required": ["error", "result"]
}

SCHEMA["getOHLCdata"] = SCHEMA["getRecentTrades"]
SCHEMA["getRecentSpreadData"] = SCHEMA["getRecentTrades"]

