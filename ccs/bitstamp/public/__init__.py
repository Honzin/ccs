# -*- coding: utf8 -*-

"""
This file implements functions for reading informations from Bitstamp public REST endpoints.
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
                Symbol is currency pair.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                last        last BTC price
                high        last 24 hours price high
                low         last 24 hours price low
                vwap        last 24 hours volume weighted average price
                volume      last 24 hours volume
                bid         highest buy order
                ask         lowest sell order
                timestamp   unix timestamp date and time
                open        first price of the day
                =========== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bitstamp.public.ticker("btcusd")
                >>> print(response)
                {
                    "high": "906.00",
                    "last": "891.32",
                    "timestamp": "1483813425",
                    "bid": "889.33",
                    "vwap": "867.24",
                    "volume": "23430.28938458",
                    "low": "812.28",
                    "ask": "891.25",
                    "open": "894.02"
                }
                >>>
                >>> # Other examples of using
                >>> ccs.bitstamp.public.ticker("btceur")
                >>> ccs.bitstamp.public.ticker("eurusd")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["ticker"]


        .. note::
                This function use REST endpoint which is described on `Bitstamp documentation <https://www.bitstamp.net/api/>`_.

                Example of GET request:

                * https://www.bitstamp.net/api/v2/ticker/btcusd/

                * https://www.bitstamp.net/api/v2/ticker/btceur/

                * https://www.bitstamp.net/api/v2/ticker/eurusd/
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# HOURLYTICKER                                                                   #
##################################################################################

def hourlyTicker(symbol):
    """
        This function provide same data as :func:`~ccs.bitstamp.public.ticker`, but values are being calculated from within an hour.

        :param String symbol:
                Symbol is currency pair.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                last        last BTC price
                high        last hour price high
                low         last hour price low
                vwap        last hour volume weighted average price
                volume      last hour volume
                bid         highest buy order in actual hour
                ask         lowest sell order in actual hour
                timestamp   unix timestamp date and time
                open        first price of the hour
                =========== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bitstamp.public.hourlyTicker("btcusd")
                >>> print(response)
                {
                    "high": "906.00",
                    "last": "890.02",
                    "timestamp": "1483813890",
                    "bid": "890.02",
                    "vwap": "866.95",
                    "volume": "23326.63588417",
                    "low": "812.28",
                    "ask": "890.84",
                    "open": "904.95"
                }
                >>>
                >>> # Other examples of using
                >>> ccs.bitstamp.public.hourlyTicker("btceur")
                >>> ccs.bitstamp.public.hourlyTicker("eurusd")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["hourlyTicker"]


        .. note::
                This function use REST endpoint which is described on `Bitstamp documentation <https://www.bitstamp.net/api/>`_.

                Example of GET request:

                * https://www.bitstamp.net/api/v2/ticker_hour/btcusd/

                * https://www.bitstamp.net/api/v2/ticker_hour/btceur/

                * https://www.bitstamp.net/api/v2/ticker_hour/eurusd/
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRANSACTIONS                                                                   #
##################################################################################

def transactions(symbol, time=None):
    """
        This function provide history of trades.

        :param String symbol:
                Symbol is currency pair.

        :param Integer time:
                It is Unix timestamp. Setting this argument cause showing trades at or after the time. This argument is optional.

        :return:
                The function return payload of http response. It is string which contains json array of objects. One object (dictionary) represents one trade. Official description of keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                date        Unix timestamp date and time
                tid	        transaction ID
                price	    price
                type	    0 (buy) or 1 (sell)
                =========== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bitstamp.public.transactions("btcusd")
                >>> print(response)
                [
                    {
                        "date": "1483816802",
                        "tid": "12911918",
                        "price": "898.01",
                        "type": "1",
                        "amount": "1.36000000"
                    },
                    {
                        "date": "1483816801",
                        "tid": "12911917",
                        "price": "898.03",
                        "type": "1",
                        "amount": "0.15000000"
                    },
                    ...
                ]
                >>>
                >>> # Other examples of using
                >>> ccs.bitstamp.public.transactions("btceur", time=1483813890)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["transactions"]


        .. note::
                This function use REST endpoint which is described on `Bitstamp documentation <https://www.bitstamp.net/api/>`_.

                Example of GET request:

                * https://www.bitstamp.net/api/v2/transactions/btcusd/

                * https://www.bitstamp.net/api/v2/transactions/btcusd/?time=1483813890
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}

    if time:
        params["time"] = time

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def orderbook(symbol):
    """
        This function provide actual lists of orders for sell and buy.

        :param String symbol:
                Symbol is currency pair.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of object's keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                timestamp   unix timestamp
                asks        list of sell orders
                bids        list of buy orders
                =========== ===================================================

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
                >>> response = ccs.bitstamp.public.orderbook("btcusd")
                >>> print(response)
                {
                    "timestamp": "1483817361",
                     "bids":
                        [
                            ["898.01", "7.55654329"],
                            ["898.00", "2.24298440"],
                            ...
                        ],
                    "asks":
                        [
                            ["898.51", "59.81171580"],
                            ["898.52", "0.19552560"],
                            ...
                        ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["orderbook"]


        .. note::
                This function use REST endpoint which is described on `Bitstamp documentation <https://www.bitstamp.net/api/>`_.

                Example of GET request:

                * https://www.bitstamp.net/api/v2/order_book/btcusd/

                * https://www.bitstamp.net/api/v2/order_book/btceur/

                * https://www.bitstamp.net/api/v2/order_book/eurusd/
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# EUR USD CONVERSIONRATE                                                         #
##################################################################################

def eurUsdConversionRate():
    """
        This function provide conversion rate between EUR and USD.

        :param String symbol:
                Symbol is currency pair.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of object's keys is in the table.

                =========== ===================================================
                Key         Description
                =========== ===================================================
                sell        price USD -> EUR
                buy         price EUR -> USDaa
                =========== ===================================================


        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bitstamp.public.eurUsdConversionRate()
                >>> print(response)
                {
                    "sell": "1.0548",
                    "buy": "1.0624"
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["eurUsdConversionRate"]


        .. note::
                This function use REST endpoint which is described on `Bitstamp documentation <https://www.bitstamp.net/api/>`_.

                Example of GET request:

                * https://www.bitstamp.net/api/eur_usd/
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

