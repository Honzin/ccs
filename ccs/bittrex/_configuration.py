# -*- coding: utf8 -*-

"""
This file contains configuration for Bittrex stock.
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


HOSTNAME = "bittrex.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["getMarketSummary"] = "/api/v1.1/public/getmarketsummary?"
REQUESTS["getMarketHistory"] = "/api/v1.1/public/getmarkethistory?"
REQUESTS["getOrderbook"] = "/api/v1.1/public/getorderbook?"
REQUESTS["getMarkets"] = "/api/v1.1/public/getmarkets"
REQUESTS["getCurrencies"] = "/api/v1.1/public/getcurrencies"
REQUESTS["getTicker"] = "/api/v1.1/public/getticker?"
REQUESTS["getMarketSummaries"] = "/api/v1.1/public/getmarketsummaries"


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

MAPPING[constants.TICKER] = {constants.LOW: 'Low',
                             constants.HIGH: 'High',
                             constants.ASK: 'Ask',
                             constants.BID: 'Bid',
                             constants.LAST: 'Last',
                             constants.VOLUME24H: 'Volume',
                             constants.TIMESTAMP: 'TimeStamp'}

default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

MAPPING[constants.TRADE] = {constants.TID: "Id",
                            constants.PRICE: "Price",
                            constants.AMOUNT: "Quantity",
                            constants.TIMESTAMP: "TimeStamp",
                            constants.TYPE: "OrderType"}

default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = {constants.BUY: "BUY", constants.SELL: "SELL"}

# ORDERBOOK #######################################################################


MAPPING[constants.ORDERBOOK] = {constants.ASKS: 'sell', constants.BIDS: 'buy'}

MAPPING[constants.ORDER] = {}
default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

# IMRPOVE
# opravit konec .*
TIMESTAMP_PATTERN = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.*?'

# TICKER #########################################################################

SCHEMA[constants.UNIFICATED_TICKER] = {
    "type": "object",
    "properties": {
        "MarketName":       {"type": "string"},
        "High":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Low":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Volume":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Last":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "BaseVolume":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "TimeStamp":        {"type": "string", "pattern": TIMESTAMP_PATTERN},
        "Bid":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Ask":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "OpenBuyOrders":    {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
        "OpenSellOrders":   {"type": ["string", "integer"], "pattern": constants.NUMBER_PATTERN},
        "PrevDay":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Created":          {"type": "string", "pattern": TIMESTAMP_PATTERN}
    },
    "required": ["MarketName", "High", "Low", "Volume", "Last", "BaseVolume", "TimeStamp", "Bid", "Ask", "OpenBuyOrders", "OpenSellOrders", "PrevDay", "Created"]
}

SCHEMA["getMarketSummary"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "array",
            "items": SCHEMA[constants.UNIFICATED_TICKER]
        }
    },
    "required": ["success", "message", "result"]
}


# TRADES #########################################################################

SCHEMA[constants.UNIFICATED_TRADE] = {
        "type": "object",
        "properties": {
            "Id":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "Price":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "Quantity":     {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "OrderType":    {"type": "string", "enum": ["SELL", "BUY"]},
            "Total":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
            "FillType":     {"type": "string"},
            "TimeStamp":    {"type": "string", "pattern": TIMESTAMP_PATTERN}
        },
        "required": ["Id", "Price", "Quantity", "OrderType", "Total", "FillType", "TimeStamp"]
    }

SCHEMA[constants.UNIFICATED_TRADES] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_TRADE]
}

SCHEMA["getMarketHistory"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": SCHEMA[constants.UNIFICATED_TRADES]
    },
    "required": ["success", "message", "result"]
}

# ORDERBOOK #######################################################################

SCHEMA[constants.UNIFICATED_ORDER] = {
    "type": "object",
    "properties": {
        "Rate":        {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
        "Quantity":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
    },
    "required": ["Rate", "Quantity"]
}

SCHEMA[constants.UNIFICATED_ORDERS] = {
    "type": "array",
    "items": SCHEMA[constants.UNIFICATED_ORDER]
}

SCHEMA[constants.UNIFICATED_ORDERBOOK] = {
    "type": "object",
    "properties": {
        "buy":  SCHEMA[constants.UNIFICATED_ORDERS],
        "sell": SCHEMA[constants.UNIFICATED_ORDERS]
    },
    "required": ["buy", "sell"],
}

SCHEMA["getOrderbook"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": SCHEMA[constants.UNIFICATED_ORDERBOOK]
    },
    "required": ["success", "message", "result"]
}

# ORDERBOOK BUY SELL #######################################################################

SCHEMA["getOrderbookBuySell"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Quantity":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Rate":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
                },
                "required": ["Quantity", "Rate"]
            }
        }
    },
    "required": ["success", "message", "result"]
}

# GET MARKETS #######################################################################

SCHEMA["getMarkets"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "MarketCurrency":       {"type": "string"},
                    "BaseCurrency":         {"type": "string"},
                    "MarketCurrencyLong":   {"type": "string"},
                    "BaseCurrencyLong":     {"type": "string"},
                    "MinTradeSize":         {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "MarketName":           {"type": "string"},
                    "IsActive":             {"type": "boolean"},
                    "Created":              {"type": "string", "pattern": TIMESTAMP_PATTERN},
                    "Notice":               {},
                    "IsSponsored":          {},
                    "LogoUrl":              {"type": ["string", "null"]}
                },
                "required": ["MarketCurrency", "BaseCurrency", "MarketCurrencyLong", "BaseCurrencyLong", "MinTradeSize", "MarketName", "IsActive", "Created", "Notice", "IsSponsored", "LogoUrl"]
            }
        }
    },
    "required": ["success", "message", "result"]
}

# GET CURRENCIES #######################################################################

SCHEMA["getCurrencies"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "Currency":         {"type": "string"},
                    "CurrencyLong":     {"type": "string"},
                    "MinConfirmation":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "TxFee":            {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "IsActive":         {"type": "boolean"},
                    "CoinType":         {"type": "string"},
                    "BaseAddress":      {"type": ["string", "null"]},
                    "Notice":           {}
                },
                "required": ["Currency", "CurrencyLong", "MinConfirmation", "TxFee", "IsActive", "CoinType", "BaseAddress", "Notice"]
            }
        }
    },
    "required": ["success", "message", "result"]
}

# GET TICKER #######################################################################

SCHEMA["getTicker"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "object",
            "properties": {
                "Bid":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Ask":  {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                "Last": {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN}
            },
            "required": ["Bid", "Ask", "Last"]
        }
    },
    "required": ["success", "message", "result"]
}

# GET SUMMARIES #######################################################################

SCHEMA["getMarketSummaries"] = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "message": {"type": "string"},
        "result": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "MarketName":       {"type": "string"},
                    "High":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Low":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Volume":           {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Last":             {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "BaseVolume":       {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "TimeStamp":        {"type": "string", "pattern": TIMESTAMP_PATTERN},
                    "Bid":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Ask":              {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "OpenBuyOrders":    {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "OpenSellOrders":   {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "PrevDay":          {"type": ["string", "number"], "pattern": constants.NUMBER_PATTERN},
                    "Created":          {"type": "string", "pattern": TIMESTAMP_PATTERN}
                },
                "required": ["MarketName", "High", "Low", "Volume", "Last", "BaseVolume", "TimeStamp", "Bid", "Ask", "OpenBuyOrders", "OpenSellOrders", "PrevDay", "Created"]
            }
        }
    },
    "required": ["success", "message", "result"]
}
