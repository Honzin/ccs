# -*- coding: utf8 -*-

# TODO
"""
...
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

from .constants import *

####################################################################################################################
# INITIALS                                                                                                         #
####################################################################################################################

# HOSTNAME
HOSTNAMES = {}
HOSTNAMES[BITFINEX] = "api.bitfinex.com"
HOSTNAMES[BITSTAMP] = "www.bitstamp.net"
HOSTNAMES[BITTREX] = "bittrex.com"
HOSTNAMES[BTCC] = "data.btcchina.com"
HOSTNAMES[BTCE] = "btc-e.com"
HOSTNAMES[BTER] = "data.bter.com"
HOSTNAMES[CEXIO] = "cex.io"
HOSTNAMES[KRAKEN] = "api.kraken.com"
HOSTNAMES[OKCOIN] = "www.okcoin." # USD - com, CNY - .cn
HOSTNAMES[POLONIEX] = "poloniex.com"


# REQUESTS
REQUESTS = {}

# BITFINEX
# def ticker(symbol):
# def trades(symbol, timestamp=None, limit_trades=None):
# def orderbook(symbol, group=1, limit_bids=50, limit_asks=50):
# def symbols():

REQUESTS[BITFINEX] = {}
REQUESTS[BITFINEX]["ticker"] = "/v1/pubticker/[symbol]"
REQUESTS[BITFINEX]["trades"] = "/v1/trades/[symbol]/?"
REQUESTS[BITFINEX]["orderbook"] = "/v1/book/[symbol]/?"
REQUESTS[BITFINEX]["symbols"] = "/v1/symbols/"

# Stats
# /stats/:symbol
# def stats(symbol):
REQUESTS[BITFINEX]["stats"] = "/v1/stats/[symbol]"

# Fundingbook
# /lendbook/:currency
# def fundingbook(currency):
REQUESTS[BITFINEX]["fundingbook"] = "/v1/lendbook/[currency]"

# Lends
# /lends/:currency
# def lends(currency):
REQUESTS[BITFINEX]["lends"] = "/v1/lends/[currency]"

# Symbol Details
# /symbols_details
# def symbolsDetails():
REQUESTS[BITFINEX]["symbolsDetails"] = "/v1/symbols_details"


# BITSTAMP
# def ticker():
# def transactions(time=""):
# def orderbook():

REQUESTS[BITSTAMP] = {}
REQUESTS[BITSTAMP]["ticker"] = "/api/v2/ticker/[symbol]"
REQUESTS[BITSTAMP]["transactions"] = "/api/v2/transactions/[symbol]/?"
REQUESTS[BITSTAMP]["orderbook"] = "/api/v2/order_book/[symbol]/"
REQUESTS[BITSTAMP]["hourlyTicker"] = "/api/v2/ticker_hour/[symbol]/"
REQUESTS[BITSTAMP]["eurUsdConversionRate"] = "/api/eur_usd/"
# BITTREX
# getMarketSummary(market):
# getOrderBook(market, depth=50, type="both"):
# getmarkethistory(market, count=50):

REQUESTS[BITTREX] = {}
REQUESTS[BITTREX]["getMarketSummary"] = "/api/v1.1/public/getmarketsummary?"
REQUESTS[BITTREX]["getmarkethistory"] = "/api/v1.1/public/getmarkethistory?"
REQUESTS[BITTREX]["getOrderBook"] = "/api/v1.1/public/getorderbook?"
REQUESTS[BITTREX]["getmarkets"] = "/api/v1.1/public/getmarkets"
REQUESTS[BITTREX]["getcurrencies"] = "/api/v1.1/public/getcurrencies"
REQUESTS[BITTREX]["getticker"] = "/api/v1.1/public/getticker?"
REQUESTS[BITTREX]["getmarketsummaries"] = "/api/v1.1/public/getmarketsummaries"

# BTCC
# def ticker(market):
# def trades(market):
# def orderbook(market, limit=None):

REQUESTS[BTCC] = {}
REQUESTS[BTCC]["ticker"] = "/data/ticker?"
REQUESTS[BTCC]["trades"] = "/data/trades?"
REQUESTS[BTCC]["orderbook"] = "/data/orderbook?"
REQUESTS[BTCC]["tradeHistory"] = "/data/historydata?"

# BTCE
# def ticker(pair):
# def trades(pair, limit=2000):
# def depth(pair, limit=150):
# def info():

REQUESTS[BTCE] = {}
REQUESTS[BTCE]["ticker"] = "/api/3/ticker/[symbol]"
REQUESTS[BTCE]["trades"] = "/api/3/trades/[symbol]/?"
REQUESTS[BTCE]["depth"] = "/api/3/depth/[symbol]/?"
REQUESTS[BTCE]["info"] = "/api/3/info"

# BTER
# def ticker(symbol):
# def tradeHistory(symbol):
# def depth(symbol):

REQUESTS[BTER] = {}
REQUESTS[BTER]["ticker"] = "/api/1/ticker/[symbol]"
REQUESTS[BTER]["tradeHistory"] = "/api/1/trade/[symbol]"
REQUESTS[BTER]["depth"] = "/api/1/depth/[symbol]"

# /api/1/pairs
# tradingPairs
REQUESTS[BTER]["tradingPairs"] = "/api/1/pairs"

# http://data.bter.com/api/1/marketinfo
# marketInfo
REQUESTS[BTER]["marketInfo"] = "/api/1/marketinfo"

# http://data.bter.com/api/1/marketlist
# marketDetails
REQUESTS[BTER]["marketDetails"] = "/api/1/marketlist"

# http://data.bter.com/api/1/tickers
# tickers
REQUESTS[BTER]["tickers"] = "/api/1/tickers"

# CEXIO
# def ticker(symbol):
# def tradeHistory(symbol, since=None):
# def orderbook(symbol, depth=None):

REQUESTS[CEXIO] = {}
REQUESTS[CEXIO]["ticker"] = "/api/ticker/"
REQUESTS[CEXIO]["tradeHistory"] = "/api/trade_history/"
REQUESTS[CEXIO]["orderbook"] = "/api/order_book/"
REQUESTS[CEXIO]["currencyLimits"] = "/api/currency_limits"
REQUESTS[CEXIO]["lastPrice"] = "/api/last_price/"
REQUESTS[CEXIO]["historical1mOHLCVChart"] = "/api/ohlcv/hd/"
REQUESTS[CEXIO]["tickersForAllPairsByMarket"] = "/api/tickers/"
REQUESTS[CEXIO]["lastPricesForGivenMarket"] = "/api/last_prices/"
REQUESTS[CEXIO]["convert"] = "/api/convert/"
REQUESTS[CEXIO]["chart"] = "/api/price_stats/"

# KRAKEN
# def ticker(pair):
# def getRecentTrades(pair, since=None):
# def getOrderBook(pair, count=""):
# def getTradableAssetPairs(info=None, pair=None):

REQUESTS[KRAKEN] = {}
REQUESTS[KRAKEN]["ticker"] = "/0/public/Ticker?"
REQUESTS[KRAKEN]["getRecentTrades"] = "/0/public/Trades?"
REQUESTS[KRAKEN]["getOrderBook"] = "/0/public/Depth?"
REQUESTS[KRAKEN]["getTradableAssetPairs"] = "/0/public/AssetPairs?"
REQUESTS[KRAKEN]["getServerTime"] = "/0/public/Time"
REQUESTS[KRAKEN]["getAssetInfo"] = "/0/public/Assets"
REQUESTS[KRAKEN]["getOHLCdata"] = "/0/public/OHLC?"
REQUESTS[KRAKEN]["getRecentSpreadData"] = "/0/public/Spread?"

# OKCOIN
# def ticker(symbol):
# def trades(symbol, since=1):
# def depth(symbol, size, merge=1):

REQUESTS[OKCOIN] = {}
REQUESTS[OKCOIN]["ticker"] = "/api/v1/ticker.do?"
REQUESTS[OKCOIN]["trades"] = "/api/v1/trades.do?"
REQUESTS[OKCOIN]["depth"] = "/api/v1/depth.do?"
REQUESTS[OKCOIN]["kline"] = "/api/v1/kline.do"

# POLONIEX
# def returnTicker():
# def returnTradeHistory(currencyPair, start=None, end=None):
# def returnOrderBook(currencyPair, depth=10):

REQUESTS[POLONIEX] = {}
REQUESTS[POLONIEX]["returnTicker"] = "/public?"
REQUESTS[POLONIEX]["returnTradeHistory"] = "/public?"
REQUESTS[POLONIEX]["returnOrderBook"] = "/public?"
REQUESTS[POLONIEX]["return24hVolume"] = "/public?"
REQUESTS[POLONIEX]["returnChartData"] = "/public?"
REQUESTS[POLONIEX]["returnCurrencies"] = "/public?"
REQUESTS[POLONIEX]["returnLoanOrders"] = "/public?"

# DIRECTION

# HEADER
DEFAULT_HEADER = {'Connection':     'keep-alive',
                  'Cache-Control':  'no-cache',
                  'Accept':         'application/json',
                  'Accept-Charset':  UTF8,
                  'Content-Type':   'application/x-www-form-urlencoded'}
HEADERS = {}
HEADERS[BITFINEX] = DEFAULT_HEADER
HEADERS[BITSTAMP] = DEFAULT_HEADER
HEADERS[BTCC] = DEFAULT_HEADER
HEADERS[BITTREX] = DEFAULT_HEADER
HEADERS[BTCE] = DEFAULT_HEADER
HEADERS[BTER] = DEFAULT_HEADER
HEADERS[CEXIO] = DEFAULT_HEADER
HEADERS[KRAKEN] = DEFAULT_HEADER
HEADERS[OKCOIN] = DEFAULT_HEADER
HEADERS[POLONIEX] = DEFAULT_HEADER


# COMPRESIONS
COMPRESSIONS = {}
COMPRESSIONS[BITFINEX] = GZIP
COMPRESSIONS[BITSTAMP] = IDENTITY
COMPRESSIONS[BITTREX] = GZIP
COMPRESSIONS[BTCC] = IDENTITY
COMPRESSIONS[BTCE] = GZIP
COMPRESSIONS[BTER] = GZIP
COMPRESSIONS[CEXIO] = IDENTITY
COMPRESSIONS[KRAKEN] = GZIP
COMPRESSIONS[OKCOIN] = IDENTITY # okcoin.cn umi pouze identity
COMPRESSIONS[POLONIEX] = GZIP

# TIMEOUTS
TIMEOUTS = {}
TIMEOUTS[BITFINEX] = 20
TIMEOUTS[BITSTAMP] = 20
TIMEOUTS[BITTREX] = 20
TIMEOUTS[BTCC] = 20
TIMEOUTS[BTCE] = 20
TIMEOUTS[BTER] = 20
TIMEOUTS[CEXIO] = 20
TIMEOUTS[KRAKEN] = 20
TIMEOUTS[OKCOIN] = 20
TIMEOUTS[POLONIEX] = 20

VERBOSE = False

# LOGGER
LOGGER_NAME = "ccsVerboseLoger"
LOGGER_FORMAT = 'verbose > %(message)s '
LOGGER_TIMEFORMAT = "%Y-%m-%d %H:%M:%S"


def complete(default, extension):
    for key in default:
        if key in extension:
            continue
        else:
            extension[key] = default[key]


RAW = True

MAPPER = {}
MAPPER[DEFAULT] = {}
MAPPER[DEFAULT][TICKER] = {LOW: 'low',
                           HIGH: 'high',
                           ASK: 'ask',
                           BID: 'bid',
                           LAST: 'last',
                           VOLUME24H: 'volume24h',
                           TIMESTAMP: 'timestamp'}


##################################################################################
# TRADES                                                                         #
##################################################################################

MAPPER[BITFINEX] = {}
MAPPER[BITFINEX][TICKER] = {LAST: "last_price",
                            VOLUME24H: "volume"}

complete(MAPPER[DEFAULT][TICKER], MAPPER[BITFINEX][TICKER])


MAPPER[BITSTAMP] = {}
MAPPER[BITSTAMP][TICKER] = {VOLUME24H: "volume"}

MAPPER[BITTREX] = {}
MAPPER[BITTREX][TICKER] = {LOW: 'Low',
                           HIGH: 'High',
                           ASK: 'Ask',
                           BID: 'Bid',
                           LAST: 'Last',
                           VOLUME24H: 'Volume',
                           TIMESTAMP: 'TimeStamp'}

complete(MAPPER[DEFAULT][TICKER], MAPPER[BITTREX][TICKER])


MAPPER[BTCC] = {}
MAPPER[BTCC][TICKER] = {ASK: "buy",
                        BID: "sell",
                        VOLUME24H: "vol",
                        TIMESTAMP: "date"}

complete(MAPPER[DEFAULT][TICKER], MAPPER[BTCC][TICKER])


MAPPER[BTCE] = {}
MAPPER[BTCE][TICKER] = {ASK: "buy",
                        BID: "sell",
                        VOLUME24H: "vol",
                        TIMESTAMP: "updated"}

complete(MAPPER[DEFAULT][TICKER], MAPPER[BTCE][TICKER])

MAPPER[BTER] = {}
MAPPER[BTER][TICKER] = {ASK: "buy",
                        BID: "sell"}

# Volume24h - upraveno v metode
# Timestamp - upraveno v metode
complete(MAPPER[DEFAULT][TICKER], MAPPER[BTER][TICKER])


MAPPER[CEXIO] = {}
MAPPER[CEXIO][TICKER] = {VOLUME24H: "volume"}

complete(MAPPER[DEFAULT][TICKER], MAPPER[CEXIO][TICKER])

MAPPER[KRAKEN] = {}
MAPPER[KRAKEN][TICKER] = {LOW: 'l',
                          HIGH: 'h',
                          ASK: "a",
                          BID: "b",
                          LAST: "c",
                          VOLUME24H: "v",
                          TIMESTAMP: None}

complete(MAPPER[DEFAULT][TICKER], MAPPER[KRAKEN][TICKER])

MAPPER[OKCOIN] = {}
MAPPER[OKCOIN][TICKER] = {ASK: "buy",
                          BID: "sell",
                          VOLUME24H: "vol"}

complete(MAPPER[DEFAULT][TICKER], MAPPER[OKCOIN][TICKER])


MAPPER[POLONIEX] = {}
MAPPER[POLONIEX][TICKER] = {LOW: "low24hr",
                            HIGH: "high24hr",
                            ASK: "lowestAsk",
                            BID: "highestBid",
                            LAST: "last",
                            VOLUME24H: "baseVolume"}
# quoteVolume ?
# timestamp emul

##################################################################################
# TRADE                                                                          #
##################################################################################

MAPPER[DEFAULT][TRADE] = {TID: "tid",
                          PRICE: "price",
                          AMOUNT: "amount",
                          TIMESTAMP: "timestamp"}

MAPPER[BITFINEX][TRADE] = {TYPE: "type"}
complete(MAPPER[DEFAULT][TRADE], MAPPER[BITFINEX][TRADE])


MAPPER[BITSTAMP][TRADE] = {TYPE: "type", TIMESTAMP: "date"}

complete(MAPPER[DEFAULT][TRADE], MAPPER[BITSTAMP][TRADE])

# {"success":true,"message":"","result":[{"Id":3937197,"TimeStamp":"2016-12-07T16:38:09.407","Quantity":25682.95434300,"Price":0.00000028,"Total":0.00719122,"FillType":"FILL","OrderType":"BUY"},
# {"Id":3937196,"TimeStamp":"2016-12-07T16:38:09.407","Quantity":70042.99000000,"Price":0.00000028,"Total":0.01961203,"FillType":"PARTIAL_FILL","OrderType":"BUY"}]}

MAPPER[BITTREX][TRADE] = {TID: "Id",
                          PRICE: "Price",
                          AMOUNT: "Quantity",
                          TIMESTAMP: "TimeStamp",
                          TYPE: "OrderType"}


MAPPER[BTCC][TRADE] = {TIMESTAMP: "date"}

complete(MAPPER[DEFAULT][TRADE], MAPPER[BTCC][TRADE])

MAPPER[BTCE][TRADE] = {TYPE: "type"}
complete(MAPPER[DEFAULT][TRADE], MAPPER[BTCE][TRADE])

# {"result":"true","data":[{"date":"1481128134","price":5323.44,"amount":0.004,"tid":"351129","type":"sell"},{"date":"1481128141","price":5323.61,"amount":0.028,"tid":"351130","type":"sell"}],"elapsed":"0.089ms"}

MAPPER[BTER][TRADE] = {TIMESTAMP: "date", TYPE: "type"}
complete(MAPPER[DEFAULT][TRADE], MAPPER[BTER][TRADE])

MAPPER[CEXIO][TRADE] = {TIMESTAMP: "date", TYPE: "type"}
complete(MAPPER[DEFAULT][TRADE], MAPPER[CEXIO][TRADE])

MAPPER[KRAKEN][TRADE] = {PRICE: 0,
                         AMOUNT: 1,
                         TIMESTAMP: 2,
                         TYPE: 3}

MAPPER[OKCOIN][TRADE] = {TYPE: "type", TIMESTAMP: "date"}
complete(MAPPER[DEFAULT][TRADE], MAPPER[OKCOIN][TRADE])

# [{"globalTradeID":68172545,"tradeID":2209360,"date":"2016-12-07 17:12:17","type":"sell","rate":"0.00470928","amount":"0.03746884","total":"0.00017645"},
# {"globalTradeID":68172456,"tradeID":2209359,"date":"2016-12-07 17:11:43","type":"sell","rate":"0.00470926","amount":"0.02237958","total":"0.00010539"}]

MAPPER[POLONIEX][TRADE] = {TID: "globalTradeID",
                           PRICE: "rate",
                           AMOUNT: "amount",
                           TIMESTAMP: "date",
                           TYPE: "type"}

#MAPPER[DEFAULT][TRADE_TYPE]  = {BUY: "buy", SELL: "sell"}
MAPPER[BITFINEX][TRADE_TYPE] = {BUY: "buy", SELL: "sell"}
MAPPER[BITSTAMP][TRADE_TYPE] = {BUY: "0", SELL: "1"}
MAPPER[BITTREX][TRADE_TYPE] = {BUY: "BUY", SELL: "SELL"}
# BTCC HASNT TYPE
MAPPER[BTCC][TRADE_TYPE] = {}
MAPPER[BTCE][TRADE_TYPE] = {BUY: "bid", SELL: "ask"}
MAPPER[BTER][TRADE_TYPE] = {BUY: "buy", SELL: "sell"}
MAPPER[CEXIO][TRADE_TYPE] = {BUY: "buy", SELL: "sell"}
MAPPER[KRAKEN][TRADE_TYPE] = {BUY: "b", SELL: "s"}
MAPPER[OKCOIN][TRADE_TYPE]  = {BUY: "buy", SELL: "sell"}
MAPPER[POLONIEX][TRADE_TYPE]  = {BUY: "buy", SELL: "sell"}

##################################################################################
# ORDERBOOK                                                                      #
##################################################################################


MAPPER[DEFAULT][ORDER] = {PRICE: "price", AMOUNT: "amount"}

MAPPER[BITFINEX][ORDER] = {}
complete(MAPPER[DEFAULT][ORDER], MAPPER[BITFINEX][ORDER])

MAPPER[BITSTAMP][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[BITTREX][ORDERBOOK] = {ASKS: 'sell', BIDS: 'buy'} # tohle je ale asi opacne
MAPPER[BITTREX][ORDER] = {PRICE: 'Rate', AMOUNT: 'Quantity'}
MAPPER[BTCC][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[BTCE][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[BTER][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[CEXIO][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[KRAKEN][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[OKCOIN][ORDER] = {PRICE: 0, AMOUNT: 1}
MAPPER[POLONIEX][ORDER] = {PRICE: 0, AMOUNT: 1}