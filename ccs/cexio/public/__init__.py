# -*- coding: utf8 -*-

"""
This file contains configuration for Cexio stock.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

import urllib.parse
import sys
import datetime

from ... import core
from ... import constants
from . import response

##################################################################################
# TICKER                                                                         #
##################################################################################

def ticker(cur1, cur2):
    """
         This function provide tick data. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                timestamp   unix timestamp
                low         last 24 hours price low
                high        last 24 hours price high
                last        last BTC price
                volume      last 24 hours volume
                volume30d   last 30 days volume
                bid         highest buy order
                ask         lowest sell order
                =========== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.cexio.public.ticker("BTC", "USD")
                >>> print(response)
                {
                    "timestamp":"1483867160",
                    "low":"833",
                    "high":"946.767",
                    "last":"937.0052",
                    "volume":"633.06282323",
                    "volume30d":"16484.96095494",
                    "bid":937.0051,
                    "ask":937.5979
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["ticker"]


        .. note::
                This function use REST endpoint which is described on `Cexio Ticker documentation <https://cex.io/rest-api#ticker>`_.

                Example of GET request:

                * https://cex.io/api/ticker/BTC/USD
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip() # TODO BTC/USD takhle to nemuze zustat

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADE HISTORY                                                                  #
##################################################################################

def tradeHistory(cur1, cur2, since=None):
    """
        This function provide history of trades.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param Integer since:
                Value of this argument is tid. Setting this argument cause showing trades with equal or higher tid. This argument is optional.

        :return:
                The function return payload of http response. It is string which contains json array of objects. Each object describe one trade. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                tid         unique trade id
                type        buy or sell
                amount      trade amount
                price       price
                date        Unix timestamp
                =========== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.cexio.public.tradeHistory("BTC", "USD")
                >>> print(response)
                [
                    {
                        "type":"buy",
                        "date":"1483867726",
                        "amount":"0.13000000",
                        "price":"937.0051",
                        "tid":"1979261"
                    },
                    {
                        "type":"sell",
                        "date":"1483867558",
                        "amount":"0.06504816",
                        "price":"935.8778",
                        "tid":"1979260"
                    },
                    ...
                ]
                >>>
                >>> # Other examples of using
                >>> ccs.cexio.public.tradeHistory("BTC", "USD", since=1)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["tradeHistory"]

        .. note::
                This function use REST endpoint which is described on `Cexio Trades history documentation <https://cex.io/rest-api#trade-history>`_.

                Example of GET request:

                * https://cex.io/api/trade_history/BTC/USD/

                * https://cex.io/api/trade_history/BTC/USD/?since=1
   """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip() + '/?' + urllib.parse.urlencode(params) # TODO BTC/USD takhle to nemuze zustat

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def orderbook(cur1, cur2, depth=None):
    """
        This function provide actual lists of orders for sell and buy.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param Integer depth:
                 It define maximum number of asks / bids. This argument is optional.

        :return:
                The function return payload of http response. It is string which contains json object on top level. Official description of keys is in the table.

                =========== ============================================================================================
                Key         Description
                =========== ============================================================================================
                timestamp   Unix timestamp
                bids        lists of open orders, each order is represented as a list
                asks        lists of open orders, each order is represented as a list
                pair        pair name
                id          incremental version id of order-book snapshot, may be used to check changes
                sell_total  total available in symbol1 (cur1)
                buy_total   total available in symbol2 (cur2)
                =========== ============================================================================================

                Each item in arrays for asks and bids describe one order. Official description of array position is in the table.

                ========= =========================
                Position  Description
                ========= =========================
                0         price
                1         volume
                ========= =========================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.cexio.public.orderbook("BTC", "USD")
                >>> print(response)
                {
                    "timestamp":1483868324,
                    "bids":
                            [
                                [938.0029,0.05900835],
                                [938.0027,0.01000000],
                                ...
                            ],
                    "asks":
                            [
                                [940.0000,0.13479788],
                                [941.1730,1.88500000],
                                ...
                            ],
                    "pair":"BTC:USD",
                    "id":26236005,
                    "sell_total":"1212.64829285",
                    "buy_total":"1293393.16"
                }
                >>>
                >>> # Other examples of using
                >>> ccs.cexio.public.orderbook("BTC", "USD", depth=1)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["orderbook"]

        .. note::
                This function use REST endpoint which is described on `Cexio Orderbook documentation <https://cex.io/rest-api#orderbook>`_.

                Example of GET request:

                * https://cex.io/api/order_book/BTC/USD/

                * https://cex.io/api/order_book/BTC/USD/?depth=1
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if depth:
        params["depth"] = depth

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip() + '/?' + urllib.parse.urlencode(params) # TODO BTC/USD takhle to nemuze zustat

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# CURRENCY LIMITS                                                                #
##################################################################################

def currencyLimits():
    """
       This function provide limits for all pairs.

       :return:
               The function return payload of http response. It is string which contains json objects. Each object describe one pair. Official description of keys is in the table.

               ============ ===================================================
               Key          Description
               ============ ===================================================
               symbol1      ?
               symbol2      ?
               minLotSize   ?
               minLotSizeS2 ?
               maxLotSize   ?
               minPrice     ?
               maxPrice     ?
               ============ ===================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.currencyLimits()
               >>> print(response)
               {
                    "e":"currency_limits",
                    "ok":"ok",
                    "data":
                            {
                                "pairs":
                                        [
                                            {
                                                "symbol1":"BTC",
                                                "symbol2":"USD",
                                                "minLotSize":0.01,
                                                "minLotSizeS2":2.5,
                                                "maxLotSize":30,
                                                "minPrice":"1",
                                                "maxPrice":"4096"
                                            },
                                            {
                                                "symbol1":"BTC",
                                                "symbol2":"EUR",
                                                "minLotSize":0.01,
                                                "minLotSizeS2":2.2,
                                                "maxLotSize":30,
                                                "minPrice":"100.00",
                                                "maxPrice":"1900.00"
                                            },
                                            ...
                                        ]
                            }
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["currencyLimits"]


       .. note::
               This function use REST endpoint which is described on `Cexio Currency limits documentation <https://cex.io/rest-api#currency-limits>`_.

               Example of GET request:

               * https://cex.io/api/currency_limits
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TICKERS FOR ALL PAIRS BY MARKET                                                #
##################################################################################

def tickersForAllPairsByMarket(*args):
    """
        This function provide tick information for required markets.

       :param Array args:
            It is array of strings, which contain name of currencies. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

       :return:
               The function return payload of http response. It is string which contains json objects. Each object describe one ticker for one pair. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                timestamp   unix timestamp
                low         last 24 hours price low
                high        last 24 hours price high
                last        last BTC price
                volume      last 24 hours volume
                volume30d   last 30 days volume
                bid         highest buy order
                ask         lowest sell order
                =========== ===================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.tickersForAllPairsByMarket("USD", "EUR", "RUB", "BTC")
               >>> print(response)
               {
                    "e":"tickers",
                    "ok":"ok",
                    "data":
                            [
                                {
                                    "timestamp":"1483871358",
                                    "pair":"BTC:USD",
                                    "low":"842.618",
                                    "high":"946.767",
                                    "last":"937.545",
                                    "volume":"628.64061219",
                                    "volume30d":"16462.50176059",
                                    "bid":937.5473,
                                    "ask":938.9099
                                },
                                {
                                    "timestamp":"1483871358",
                                    "pair":"LTC:USD",
                                    "low":"3.6637",
                                    "high":"4.104499",
                                    "last":"4.0129",
                                    "volume":"299.11955482",
                                    "volume30d":"12250.58086773",
                                    "bid":3.963,
                                    "ask":4.04699999
                                },
                                ...
                            ]
                }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["tickersForAllPairsByMarket"]


       .. note::
               This function use REST endpoint which is described on `Cexio Ticker for all pairs documentation <https://cex.io/rest-api#tickers-all>`_.

               Example of GET request:

               * https://cex.io/api/tickers/USD/EUR/RUB/BTC
   """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    suffix = ""
    for a in args:
        suffix += a + "/"

    # complete request
    cr = core.request(s, r) + suffix

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# LAST PRICE                                                                     #
##################################################################################

def lastPrice(cur1, cur2):
    """
        This function provide last price for given market.

       :param String cur1:
               It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

       :param String cur2:
               It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

       :return:
               The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

               =========== ===========================================================================
               Key         Description
               =========== ===========================================================================
               curr1       the first currency code;
               curr2       the second currency code;
               lprice      last price of selling/buying the first currency relative to the second one
               =========== ===========================================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.lastPrice("BTC", "USD")
               >>> print(response)
               {
                    "lprice":"937.545",
                    "curr1":"BTC",
                    "curr2":"USD"
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["lastPrice"]


       .. note::
               This function use REST endpoint which is described on `Cexio Last price documentation <https://cex.io/rest-api#lprice>`_.

               Example of GET request:

               * https://cex.io/api/last_price/BTC/USD
   """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip() # TODO BTC/USD takhle to nemuze zustat

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# LAST PRICE FOR GIVEN MARKET                                                    #
##################################################################################

def lastPricesForGivenMarket(*args):
    """
        This function provide last price for required markets.

       :param Array args:
            It is array of strings, which contain name of currencies. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

       :return:
               The function return payload of http response. It is string which contains json objects. Each object describe one ticker for one pair. Official description of keys is in the table.

               =========== ===========================================================================
               Key         Description
               =========== ===========================================================================
               symbol1     the first currency code;
               symbol2     the second currency code;
               lprice      last price of selling/buying the first currency relative to the second one
               =========== ===========================================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.lastPricesForGivenMarket("BTC", "USD", "LTC")
               >>> print(response)
               {
                    "e":"last_prices",
                    "ok":"ok",
                    "data":
                            [
                                {
                                    "symbol1":"BTC",
                                    "symbol2":"USD",
                                    "lprice":"937.545"
                                },
                                {
                                    "symbol1":"LTC",
                                    "symbol2":"USD",
                                    "lprice":"4.0129"
                                },
                                ...
                            ]
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["lastPricesForGivenMarket"]


       .. note::
               This function use REST endpoint which is described on `Cexio Last price for given market documentation <https://cex.io/rest-api#lprice-all>`_.

               Example of GET request:

               * https://cex.io/api/last_prices/BTC/USD/LTC
   """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    suffix = ""
    for a in args:
        suffix += a + "/"

    # complete request
    cr = core.request(s, r) + suffix

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# CONVERT                                                                        #
##################################################################################

def convert(cur1, cur2, amnt):
    """
        This function converts any amount of the currency to any other currency by multiplying the amount by the last price of the chosen pair according to the current exchange rate.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param Integer amnt:
                Amount of convertible currency.

       :return:
               The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

               =========== ===========================================================================
               Key         Description
               =========== ===========================================================================
               amnt        amount in the target currency
               =========== ===========================================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
                >>> import ccs
                >>> response = ccs.cexio.public.convert("BTC", "USD", 2.5)
                >>> print(response)
                {
                    "amnt":2060.5
                }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["convert"]


       .. note::
               This function use REST endpoint which is described on `Cexio Convert documentation <https://cex.io/rest-api#converter>`_.

                Here is not example, because this request is executed by POST method.
   """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["amnt"] = amnt

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip() # + ''

    return core.post(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s), urllib.parse.urlencode(params))


##################################################################################
# CHART                                                                          #
##################################################################################

def chart(cur1, cur2, lastHours, maxRespArrSize):
    """
        This function allows building price change charts (daily, weekly, monthly) and showing historical point in any point of the chart.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param Integer lastHours:
                Past tense period till the current date in hours.

        :param Integer maxRespArrSize:
                Maximal amount of price values in return.

       :return:
               The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

               =========== ===========================================================================
               Key         Description
               =========== ===========================================================================
               tmsp        UNIX timestamp
               price       price value
               =========== ===========================================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.chart("BTC", "USD", 24, 100)
               >>> print(response)
               [
                   {
                       "tmsp":1482246000,
                       "price":"796.658"
                   },
                   {
                       "tmsp":1482246900,
                       "price":"796.1659"
                   },
                   ...
               ]
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["chart"]


       .. note::
               This function use REST endpoint which is described on `Cexio Chart documentation <https://cex.io/rest-api#chart>`_.

                Here is not example, because this request is executed by POST method.
   """

    s = __name__.split(".")[1]          # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["lastHours"] = lastHours
    params["maxRespArrSize"] = maxRespArrSize

    # complete request
    cr = core.request(s, r) + cur1.upper().strip() + '/' + cur2.upper().strip()

    return core.post(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s), urllib.parse.urlencode(params))


##################################################################################
# HISTORICAL 1M OHLC CHART                                                       #
##################################################################################

def historical1mOHLCVChart(cur1, cur2, year, month, day):
    """
        This function provides dataset to build 1m OHLCV chart for a given date. Relies on historical data, is not working for current date.

        :param String cur1:
                It is base currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param String cur2:
                It is quote currency. For more information about available currencies visit :func:`~ccs.cexio.public.currencyLimits`.

        :param Integer year:
                Integer value which represent year.

        :param Integer month:
                Integer value which represent month.

        :param Integer day:
                Integer value which represent day.

       :return:
               The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

               =========== ===========================================================================
               Key         Description
               =========== ===========================================================================
               time        Unix timestamp
               data1m      1440 candle data sets
               =========== ===========================================================================

                Each item in arrays describe one 1m candle. Official description of array position is in the table.

                ========= =========================
                Position  Description
                ========= =========================
                0         Unix timestamp
                1         open price
                2         high price
                3         low price
                4         close price
                5         volume
                ========= =========================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.cexio.public.historical1mOHLCVChart("BTC", "USD", 2016, 2, 28)
               >>> print(response)
               {
                    "time":20160228,
                    "data1m":"
                            [
                                [1456617600,434.3867,434.3867,433.781,433.781,4.15450000],
                                [1456617660,433.747,433.747,433.7306,433.7306,3.00010001],
                                ...
                            ]
                            "
                }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.CEXIO]["historical1mOHLCVChart"]


       .. note::
               This function use REST endpoint which is described on `Cexio Historical 1m OHLCV Chart  documentation <https://cex.io/rest-api#minute-chart>`_.

                Example of GET request:

                * https://cex.io/api/ohlcv/hd/20160228/BTC/USD
   """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    dt = datetime.datetime(year, month, day)

    # complete request
    cr = core.request(s, r) + dt.strftime("%Y%m%d") + "/" + cur1.upper().strip() + '/' + cur2.upper().strip() # TODO BTC/USD takhle to nemuze zustat

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

