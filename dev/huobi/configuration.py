from ccs import constants
from ccs import default

##################################################################################
# HOSTNAME                                                                       #
##################################################################################


HOSTNAME = "api.huobi.com"

##################################################################################
# REQUEST                                                                        #
##################################################################################

REQUESTS = {}
REQUESTS["kline"] = "/[cur2]market/[cur1]_kline_[period]_json.js"
REQUESTS["ticker"] = "/[cur2]market/ticker_[cur1]_json.js"
REQUESTS["depth"] = "/[cur2]market/depth_[cur1]_json.js"
REQUESTS["detail"] = "/[cur2]market/detail_[cur1]_json.js"

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

# DEFAULT
# TICKER = {LOW: 'low',
#           HIGH: 'high',
#           ASK: 'ask',
#           BID: 'bid',
#           LAST: 'last',
#           VOLUME24H: 'volume24h',
#           TIMESTAMP: 'timestamp'}

MAPPING[constants.TICKER] = {}
default.complete(default.TICKER, MAPPING[constants.TICKER])

# TRADES #########################################################################

# DEFAULT
# TRADE = {TID: "tid",
#          PRICE: "price",
#          AMOUNT: "amount",
#          TIMESTAMP: "timestamp"}

MAPPING[constants.TRADE] = {}
default.complete(default.TRADE, MAPPING[constants.TRADE])

MAPPING[constants.TRADE_TYPE] = "" #{constants.BUY: "buy", constants.SELL: "sell"}

# ORDERBOOK #######################################################################

# DEFAULT
# ORDER = {PRICE: "price", AMOUNT: "amount"}

MAPPING[constants.ORDER] = {}
default.complete(default.ORDER, MAPPING[constants.ORDER])

##################################################################################
# SCHEMA                                                                         #
##################################################################################

SCHEMA = {}

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
SCHEMA[constants.TICKER] = {}

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
SCHEMA[constants.TRADE] = {}

# {
#     "type": "array",
#     "items": SCHEMA[constants.TRADE]
# }
SCHEMA[constants.TRADES] = {}


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
SCHEMA[constants.ORDER] = {}


# {
#     "type": "array",
#     "items": SCHEMA[constants.ORDER]
# }
SCHEMA[constants.ORDERS] = {}


# {
#     "type": "object",
#     "properties": {
#         "asks": SCHEMA[constants.ORDERS],
#         "bids": SCHEMA[constants.ORDERS]
#     },
#     "required": ["asks", "bids"],
#     "additionalProperties": False
# }
SCHEMA[constants.ORDERBOOK] = {}

