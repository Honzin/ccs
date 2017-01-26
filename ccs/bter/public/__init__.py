# -*- coding: utf8 -*-

"""
This file contains configuration for Bter stock.
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

def ticker(symbol):
    """
        This function provide tick data. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

       :param String symbol:
               Symbol is currency pair. For more information about symbols visit :func:`~ccs.bter.public.tradingPairs`.

       :return:
               The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

               ======================== ===================================================
               Key                      Description
               ======================== ===================================================
               result
               last
               high
               low
               avg
               sell
               buy
               vol_btc
               vol_cny
               rate_change_percentage
               ======================== ===================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.bter.public.ticker("btc_cny")
               >>> print(response)
               {
                    "result":"true",
                    "last":6301.94,
                    "high":6440,
                    "low":6050,
                    "avg":6250.29,
                    "sell":6304.44,
                    "buy":6302.95,
                    "vol_btc":129.367,
                    "vol_cny":808581.69,
                    "rate_change_percentage":"-1.41"
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.BTER]["ticker"]


       .. note::
               This function use REST endpoint which is described on `Bter Ticker documentation <https://bter.com/api#ticker>`_.

               Example of GET request:

               * http://data.bter.com/api/1/ticker/btc_cny
   """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################

def tradeHistory(symbol):
    """
        This function provide history of trades.

        :param String symbol:
                Symbol is currency pair. For more information about symbols visit :func:`~ccs.bter.public.tradingPairs`.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                date
                price
                tid
                type
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bter.public.tradeHistory("btc_cny")
                >>> print(response)
                {
                    "result":"true",
                    "data":
                            [
                                {
                                    "date":"1483966022",
                                    "price":6345.01,
                                    "amount":0.003,
                                    "tid":"425038",
                                    "type":"sell"
                                },
                                {
                                    "date":"1483966076",
                                    "price":6347.02,
                                    "amount":0.003,
                                    "tid":"425039",
                                    "type":"buy"
                                },
                                ...
                            ],
                    "elapsed":"0.054ms"
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTER]["tradeHistory"]


        .. note::
                This function use REST endpoint which is described on `Bter History documentation <https://bter.com/api#history>`_.

                Example of GET request:

                * http://data.bter.com/api/1/trade/btc_cny
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def depth(symbol):
    """
        This function provide actual lists of orders for sell and buy.

        :param String symbol:
                Symbol is currency pair. For more information about symbols visit :func:`~ccs.bter.public.tradingPairs`.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                asks
                bids
                =================== ===================================================

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
                >>> response = ccs.bter.public.depth("btc_cny")
                >>> print(response)
                {
                    "result":"true",
                    "asks":
                            [
                                [6390.57,1],
                                [6389.63,0.8],
                                ...
                            ],
                    "bids":
                        [
                            [6300,0.501],
                            [6299.88,0.466],
                            ...
                        ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTER]["depth"]


        .. note::
                This function use REST endpoint which is described on `Bter Depth documentation <https://bter.com/api#depth>`_.

                Example of GET request:

                * http://data.bter.com/api/1/depth/btc_cny
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRAIDING PAIRS                                                                 #
##################################################################################

def tradingPairs():
    """
        This function provide list of available trading pairs (symbols).


        :return:
                The function return payload of http response. It is string which contains json array. Each item is traiding pair.

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bter.public.tradingPairs()
                >>> print(response)
                [
                    "btc_cny",
                    "ltc_cny",
                    "blk_cny",
                    "bitcny_cny",
                    "bqc_cny",
                    "btb_cny",
                    ...
                ]
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTER]["tradingPairs"]


        .. note::
                This function use REST endpoint which is described on `Bter Pairs documentation <https://bter.com/api#pairs>`_.

                Example of GET request:

                * http://data.bter.com/api/1/pairs
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# MARKET INFO                                                                    #
##################################################################################

def marketInfo():
    """
        This function provide informations about markets. Its are:

        * market's fee,

        * minimum order total amount

        * and price decimal places.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                decimal_places
                min_amount
                fee
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bter.public.marketInfo()
                >>> print(response)
                {
                    "result":"true",
                    "pairs":
                            [
                                {
                                    "btc_cny":
                                            {
                                                "decimal_places":2,
                                                "min_amount":0.5,
                                                "fee":0.2
                                            }
                                },
                                {
                                    "ltc_cny":
                                            {
                                                "decimal_places":2,
                                                "min_amount":0.5,
                                                "fee":0.2
                                            }
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTER]["marketInfo"]


        .. note::
                This function use REST endpoint which is described on `Bter Market Info documentation <https://bter.com/api#marketinfo>`_.

                Example of GET request:

                * http://data.bter.com/api/1/marketinfo
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

##################################################################################
# MARKET DETAILS                                                                 #
##################################################################################

def marketDetails():
    """
        This function provide market details. http://data.bter.com/api/1/marketlist

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                no
                symbol
                name
                name_cn
                pair
                rate
                vol_a
                vol_b
                curr_a
                curr_b
                curr_suffix
                rate_percent
                trend
                supply
                marketcap
                plot
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bter.public.marketDetails()
                >>> print(response)
                {
                    "result":"true",
                    "data":
                            [
                                {
                                    "no":1,
                                    "symbol":"ETC",
                                    "name":"Ethereum Classic",
                                    "name_cn":"\u4ee5\u592a\u7ecf\u5178",
                                    "pair":"etc_cny",
                                    "rate":"10.07",
                                    "vol_a":97079.3,
                                    "vol_b":"973,604",
                                    "curr_a":"ETC",
                                    "curr_b":"CNY",
                                    "curr_suffix":" CNY",
                                    "rate_percent":"0.90",
                                    "trend":"down",
                                    "supply":87687300,
                                    "marketcap":"883,011,111",
                                    "plot":null
                                },
                                {
                                    "no":2,
                                    "symbol":"BTC",
                                    "name":"Bitcoin",
                                    "name_cn":"\u6bd4\u7279\u5e01",
                                    "pair":"btc_cny",
                                    "rate":"6255.71",
                                    "vol_a":113.4,
                                    "vol_b":"707,601",
                                    "curr_a":"BTC",
                                    "curr_b":"CNY",
                                    "curr_suffix":" CNY",
                                    "rate_percent":"0.01",
                                    "trend":"down",
                                    "supply":5249920,
                                    "marketcap":"32,841,977,043",
                                    "plot":null
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTER]["marketDetails"]


        .. note::
                This function use REST endpoint which is described on `Bter Market details documentation <https://bter.com/api#marketlist>`_.

                Example of GET request:

                * http://data.bter.com/api/1/marketlist
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TICKERS                                                                        #
##################################################################################

def tickers():
    """
        This function provide tick data for all markets (pairs). This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

       :param String symbol:
               Symbol is currency pair. For more information about symbols visit :func:`~ccs.bter.public.tradingPairs`.

       :return:
               The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

               ======================== ===================================================
               Key                      Description
               ======================== ===================================================
               result
               last
               high
               low
               avg
               sell
               buy
               vol_btc
               vol_cny
               rate_change_percentage
               ======================== ===================================================

       :rtype:
               String

       :exception:
               It can raise any exception which can occur during using

               * :py:class:`http.client.HTTPSConnection`

               * :py:func:`http.client.HTTPSConnection.request`.

       :Example:
               >>> import ccs
               >>> response = ccs.bter.public.tickers()
               >>> print(response)
               {
                    "btc_cny":
                            {
                                "result":"true",
                                "last":6204,
                                "high":6367.49,
                                "low":6050,
                                "avg":6239.67,
                                "sell":6222.32,
                                "buy":6221.38,
                                "vol_btc":113.564,
                                "vol_cny":708601.96,
                                "rate_change_percentage":"0.64"
                            },
                    "ltc_cny":
                            {
                                "result":"true",
                                "last":27.44,
                                "high":27.88,
                                "low":27.2,
                                "avg":27.57,
                                "sell":27.5,
                                "buy":27.44,
                                "vol_ltc":2365.112,
                                "vol_cny":65205.68,
                                "rate_change_percentage":"-0.11"
                            },
                            ...
               }
               >>>
               >>> # Prepared validation schema
               >>> schema = ccs.cfg.schema[ccs.constants.BTER]["tickers"]


       .. note::
               This function use REST endpoint which is described on `Bter Tickers documentation <https://bter.com/api#tickers>`_.

               Example of GET request:

               * http://data.bter.com/api/1/tickers
   """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))