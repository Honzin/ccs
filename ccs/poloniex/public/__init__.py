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

import urllib.parse
import sys

from ... import core
from ... import constants
from . import response

##################################################################################
# TICKER                                                                         #
##################################################################################

def returnTicker():
    """
    This function provide tick data. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

    :return:
            The function return payload of http response for all markets (symbols). It is string which contains json dictionary of dictionary. Unofficial description of keys is in the table.

            ================ ==================================
            Key              Unofficial description
            ================ ==================================
            id               TODO
            last             current price
            lowestAsk        current lowest ask
            highestBid       current highest bid
            percentChange    percent change of price
            baseVolume       volume of trades in base currency
            quoteVolume      volume of trades in quote currency
            isFrozen         TODO
            high24hr         TODO
            low24hr          TODO
            ================ ==================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.poloniex.public.returnTicker()
            >>> print(response)
            {
                "BTC_1CR":
                            {
                                "id":1,
                                "last":"0.00056825",
                                "lowestAsk":"0.00056821",
                                "highestBid":"0.00051000",
                                "percentChange":"0.04266055",
                                "baseVolume":"0.75982797",
                                "quoteVolume":"1453.08528184",
                                "isFrozen":"0",
                                "high24hr":"0.00063000",
                                "low24hr":"0.00045303"
                            },
                "BTC_BBR":
                            {
                                "id":6,
                                "last":"0.00008051",
                                "lowestAsk":"0.00008065",
                                "highestBid":"0.00008050",
                                "percentChange":"-0.01372044",
                                "baseVolume":"0.53542776",
                                "quoteVolume":"6618.29854886",
                                "isFrozen":"0",
                                "high24hr":"0.00008222",
                                "low24hr":"0.00008000"
                            },
                            ...
            }
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnTicker"]

    .. note::
            This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

            Example of GET request:

            * https://poloniex.com/public?command=returnTicker

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnTicker"

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADE HISTORY                                                                  #
##################################################################################

def returnTradeHistory(currencyPair, start=None, end=None):
    """
    This function provide history of trades.

    :param String currencyPair:
             It is currency pair. For more information about each currency visit :func:`~ccs.poloniex.public.returnCurrencies`. For better imagination about pairs can be use :func:`~ccs.poloniex.public.returnTicker`.

    :param Integer start:
            Start is UNIX timestamp. All trades which will return will have timestamp equal or higher. Here is one recomandation: test your window frame (start and end).

    :param Integer end:
             End is UNIX timestamp. All trades which will return will have timestamp equal or lower. Here is one recomandation: test your window frame (start and end).

    :return:
            The function return payload of http response. It is string which contains json array with object. Each object describe one trade. Unofficial description of array position is in the table.

            ===================== ==========================================
            Key                   Description
            ===================== ==========================================
            globalTradeID         Unique ID across all markets on Poloniex
            tradeID               Unique ID for this market (currency pair)
            type                  sell or buy
            rate                  equivalent for price
            amount                amount
            total                 ?
            ===================== ==========================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.poloniex.public.returnTradeHistory("BTC_LTC")
            >>> print(response)
            [
                {
                    "globalTradeID":71118065,
                    "tradeID":1094974,
                    "date":"2016-12-26 10:25:11",
                    "type":"buy",
                    "rate":"895.70000000",
                    "amount":"0.34670496",
                    "total":"310.54363267"
                },
                {
                    "globalTradeID":71118052,
                    "tradeID":1094973,
                    "date":"2016-12-26 10:25:04",
                    "type":"buy",
                    "rate":"895.70000000",
                    "amount":"0.08561533",
                    "total":"76.68565108"
                },
                ...
            ]
            >>>
            >>> # Other examples of using
            >>> ccs.poloniex.public.returnTradeHistory("BTC_LTC", start=1410158341, end=1410499372)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnTradeHistory"]

    .. note::
            This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

            Example of GET request:

            * https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT

            * https://poloniex.com/public?command=returnTradeHistory&currencyPair=BTC_NXT&start=1410158341&end=1410499372
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnTradeHistory"
    params["currencyPair"] = currencyPair
    if start:
        params["start"] = start
    if end:
        params["end"] = end

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def returnOrderBook(currencyPair, depth=10):
    """
    This function provide actual lists of orders for sell and buy.

    :param String currencyPair:
             It is currency pair. For more information about each currency visit :func:`~ccs.poloniex.public.returnCurrencies`. For better imagination about pairs can be use :func:`~ccs.poloniex.public.returnTicker`.

    :param Integer depth:
            It define maximum number of asks / bids. Default vaule is 10.

    :return:
            The function return payload of http response. It is string which contains json object. Unofficial description of object's keys is in the table.

            ===================== ==========================================
            Key                   Description
            ===================== ==========================================
            asks                  list of orders
            bids                  list of orders
            isFrozen              ?
            seq                   ?
            ===================== ==========================================

            Each item in arrays for asks and bids describe one order. Unofficial description of array position is in the table.

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
            >>> response = ccs.poloniex.public.returnOrderBook("BTC_LTC")
            >>> print(response)
            {
                "asks":
                        [
                            ["0.00000689",4110.62513846],
                            ["0.00000690",5557.36168574],
                            ...
                        ],
                "bids":
                        [
                            ["0.00000683",34.50893119],
                            ["0.00000680",642.22946578],
                            ...
                        ],
                "isFrozen":"0",
                "seq":23364099
            }
            >>>
            >>> # Other examples of using
            >>> ccs.poloniex.public.returnOrderBook("BTC_NXT", 30)
            >>> ccs.poloniex.public.returnOrderBook("all")
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnOrderBook"]

    .. note::
            This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

            Example of GET request:

            * https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_NXT&depth=10

            * https://poloniex.com/public?command=returnOrderBook&currencyPair=all&depth=2
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnOrderBook"
    params["currencyPair"] = currencyPair
    params["depth"] = depth

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# 24h VOLUME                                                                     #
##################################################################################

def return24hVolume():
    """
       This function provide 24 hour volume for all markets and totals for primary currencies.

       :return:
               The function return payload of http response. It is string which contains json object. Unofficial escription of object's keys is in the table.

               ===================== ==========================================================================
               Key                   Description
               ===================== ==========================================================================
               <base>_<quote>        Json object contains 24 hours volumes for base and quote currency of pair.
               total<base>           Sum of volumes for base currency in last 24 hours.
               ===================== ==========================================================================

               *<base>* and <quote> represent currency like *BTC*, *LTC*, ...

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.poloniex.public.return24hVolume()
               >>> print(response)
               {
                    "BTC_BBR":
                                {
                                    "BTC":"8.21369390",
                                    "BBR":"75453.72075591"
                                },
                    "BTC_BCN":
                                {
                                    "BTC":"1.90751575",
                                    "BCN":"34161303.95809131"
                                },
                    ...,
                    "totalBTC":"26026.22129242",
                    "totalETH":"14592.70438383",
                    "totalUSDT":"5666182.79780848",
                    "totalXMR":"582.22698569",
                    "totalXUSD":"0.00000000"
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["return24hVolume"]

       .. note::
               This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

               Example of GET request:

               * https://poloniex.com/public?command=return24hVolume

       """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "return24hVolume"

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# CHART DATA                                                                     #
##################################################################################

def returnChartData(currencyPair, start, end, period=1800):
    """
       This function provide candlestick chart data.

       :param String currencyPair:
                It is currency pair. For more information about each currency visit :func:`~ccs.poloniex.public.returnCurrencies`. For better imagination about pairs can be use :func:`~ccs.poloniex.public.returnTicker`.

       :param Integer start:
                Start is UNIX timestamp. All trades which will return will have timestamp equal or higher. Here is one recomandation: test your window frame (start and end).

       :param Integer end:
                End is UNIX timestamp. All trades which will return will have timestamp equal or lower. Here is one recomandation: test your window frame (start and end).

       :param Integer period:
                Time period of one candle. Valid period values are:

                 * 300

                 * 900

                 * 1800

                 * 7200

                 * 14400

                 * 86400

                 Values are in seconds. It coincides with 5 min, 15 min, 30 min, 2 hours, 4 hours and 24 hours.

       :return:
               The function return payload of http response. It is string which contains json array with object. Each object describe one trade. Unofficial escription of object's keys is in the table.

               ===================== ============================================
               Key                   Description
               ===================== ============================================
               date                  unix timestamp
               high                  candle attribute - higher price in period
               low                   candle attribute - lower price in period
               open                  candle attribute - opening price in period
               close                 candle attribute - closing price in period
               volume                volume of base currency in period
               quoteVolume           volume of quote currency in period
               weightedAverage       weighted average in period
               ===================== ============================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.poloniex.public.returnChartData("BTC_LTC", 1405699200, 9999999999, 300)
               >>> print(response)
                [
                    {
                        "date":1405699200,
                        "high":0.01436175,
                        "low":0.0140401,
                        "open":0.01436175,
                        "close":0.01436,
                        "volume":0.39285884,
                        "quoteVolume":27.6009686,
                        "weightedAverage":0.01423351
                    },
                    {
                        "date":1405713600,
                        "high":0.0141799,
                        "low":0.0141091,
                        "open":0.01416,
                        "close":0.0141799,
                        "volume":0.17488903,
                        "quoteVolume":12.37315145,
                        "weightedAverage":0.01413455
                    },
                    ...
                ]
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnChartData"]

       .. note::
               This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

               Example of GET request:

               * https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1405699200&end=9999999999&period=14400

       """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnChartData"
    params["currencyPair"] = currencyPair
    params["period"] = period
    params["start"] = start
    params["end"] = end

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# CURRENCIES                                                                     #
##################################################################################

def returnCurrencies():
    """
        This function provide detail information about available currencies.

        :return:
                The function return payload of http response. It is string which contains json object of object. Each object describes one currency. Unofficial escription of object's keys is in the table.

                ===================== ============================================
                Key                   Description
                ===================== ============================================
                id                    unique ID
                name                  full name of currency
                txFee                 fee
                minConf               ?
                depositAddress        ?
                disabled              ?
                delisted              ?
                frozen                ?
                ===================== ============================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.poloniex.public.returnCurrencies()
               >>> print(response)
               {
                    "1CR":
                        {
                            "id":1,
                            "name":"1CRedit",
                            "txFee":"0.01000000",
                            "minConf":3,
                            "depositAddress":null,
                            "disabled":0,
                            "delisted":1,
                            "frozen":0
                        },
                        ...,
                    "BTC":
                        {
                            "id":28,
                            "name":"Bitcoin",
                            "txFee":"0.00010000",
                            "minConf":1,
                            "depositAddress":null,
                            "disabled":0,
                            "delisted":0,
                            "frozen":0
                        },
                        ...
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnCurrencies"]

       .. note::
               This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

               Example of GET request:

               * https://poloniex.com/public?command=returnCurrencies

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnCurrencies"

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# LOAN ORDERS                                                                    #
##################################################################################

# returnLoanOrders
# https://poloniex.com/public?command=returnLoanOrders&currency=BTC

def returnLoanOrders(currency):
    """
        This function provide list of loan offers and demands for a given currency.

        :param String currency:
                For more information about available currencies visit :func:`~ccs.poloniex.public.returnCurrencies`.

        :return:
                The function return payload of http response. It is string which contains json object of object. Each object describes one loan order. Unofficial escription of object's keys is in the table.

                ===================== ============================================
                Key                   Description
                ===================== ============================================
                offers
                demands
                ===================== ============================================

                IMPROVE

                ===================== ============================================
                Key                   Description
                ===================== ============================================
                rate
                amount
                rangeMin
                rangeMax
                ===================== ============================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
                >>> import ccs
                >>> response = ccs.poloniex.public.returnLoanOrders("BTC")
                >>> print(response)
                {
                    "offers":
                            [
                                {
                                    "rate":"0.00018500",
                                    "amount":"0.01487170",
                                    "rangeMin":2,
                                    "rangeMax":2
                                },
                                {
                                    "rate":"0.00018599",
                                    "amount":"0.47963188",
                                    "rangeMin":2,
                                    "rangeMax":2
                                },
                                ...
                            ],
                    "demands":
                            [
                                {
                                    "rate":"0.00012100",
                                    "amount":"28.62300354",
                                    "rangeMin":2,
                                    "rangeMax":2
                                },
                                {
                                    "rate":"0.00012000",
                                    "amount":"54.51656874",
                                    "rangeMin":2,
                                    "rangeMax":2
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.POLONIEX]["returnLoanOrders"]

       .. note::
               This function use REST endpoint which is described on `Poloniex documentation <https://poloniex.com/support/api/>`_.

               Example of GET request:

               * https://poloniex.com/public?command=returnLoanOrders&currency=BTC

    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["command"] = "returnLoanOrders"
    params["currency"] = currency

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))