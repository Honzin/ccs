# -*- coding: utf8 -*-

"""
This file implements functions for reading informations from Btcc-spot public REST endpoints.
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

def ticker(market="btccny"):
    """
        This function provide detailed data of give market. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

        :param String market:
                Market is currency pair.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== =============== ===================================================
                Key                 Value           Description
                =================== =============== ===================================================
                high                string          highest price in last 24h
                low	                string          lowest price in last 24h
                buy                 string          latest bid price
                sell                string          latest ask price
                last                string          last successful trade price
                vol                 string          total BTC volume in last 24h
                date                number          last update timestamp
                vwap                number          24 hour average filled price
                prev_close          number          yesterday's closed price
                open                number          today's opening price
                =================== =============== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btcc.public.ticker("btccny")
                >>> print(response)
                {
                    "ticker":
                            {
                                "high":"5720.00",
                                "low":"5325.01",
                                "buy":"5646.33",
                                "sell":"5647.18",
                                "last":"5646.33",
                                "vol":"886404.27650000",
                                "date":1484389306,
                                "vwap":"5654",
                                "prev_close":"5625.78",
                                "open":"5625.98"
                            }
                }
                >>>
                >>> # Other examples of using
                >>> ccs.btcc.public.ticker("ltccny")
                >>> ccs.btcc.public.ticker("all")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCC]["ticker"]


        .. note::
                This function use REST endpoint which is described on `Btcc-spot Ticker documentation <https://www.btcc.com/apidocs/spot-exchange-market-data-rest-api#ticker>`_.

                Example of GET request:

                * https://data.btcchina.com/data/ticker?market=all

                * https://data.btcchina.com/data/ticker?market=btccny

                * https://data.btcchina.com/data/ticker?market=ltccny
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################

def trades(market="btccny"):
    """
        This function provide list of trades processed within the last 24h, but maximal number of trades returned is 10000.

        :param String market:
                Market is currency pair.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== =============== ===================================================
                Key                 Value           Description
                =================== =============== ===================================================
                date                string          unix time in seconds since 1 January 1970
                price               string          price for 1 BTC
                amount              string          amount of BTC traded
                tid                 string          trade id
                =================== =============== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btcc.public.trades("btccny")
                >>> print(response)
                [
                    {
                        "date":"1484372797",
                        "price":5615.41,
                        "amount":0.029,
                        "tid":"121266656"
                    },
                    {
                        "date":"1484372797",
                        "price":5615.53,
                        "amount":0.371,
                        "tid":"121266657"
                    },
                    ...
                ]
                >>>
                >>> # Other examples of using
                >>> ccs.btcc.public.trades("ltccny")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCC]["trades"]


        .. note::
                This function use REST endpoint which is described on `Btcc-spot Trades documentation <https://www.btcc.com/apidocs/spot-exchange-market-data-rest-api#trades>`_.

                Example of GET request:

                * https://data.btcchina.com/data/trades?market=btccny

                * https://data.btcchina.com/data/trades?market=ltccny
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADE HISTORY                                                                  #
##################################################################################

def tradeHistory(market="btccny", limit=100, since=None, sincetype=None):
    """
        This function provide history of trades.

        :param String market:
                Market is currency pair.

        :param Integer limit:
                It define maximum number of trades. This argument must be greater or equal to 1. This argument is optional. Default value is 100. Maximum is 5000.

        :param Integer since:
                 Setting this argument cause showing trades at or after the timestamp or tid. This argument is optional.

        :param Integer sincetype:
                 Available values for this argument are “id” or “time”. It specifies on which data the “since” parameter works. The default value is “id”.


        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== =============== ===================================================
                Key                 Value           Description
                =================== =============== ===================================================
                date                string          unix time in seconds since 1 January 1970
                price               string          price for 1 BTC
                amount              string          amount of BTC traded
                tid                 string          trade id
                type                string          indicate 'buy' or 'sell' trade
                =================== =============== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btcc.public.tradeHistory("btccny")
                >>> print(response)
                [
                    {
                        "date":"1484395859",
                        "price":5679.94,
                        "amount":0.064,
                        "tid":"121327921",
                        "type":"buy"
                    },
                    {
                        "date":"1484395859",
                        "price":5680.67,
                        "amount":0.025,
                        "tid":"121327922",
                        "type":"buy"
                    },
                    ...
                ]
                >>>
                >>> # Other examples of using
                >>> ccs.btcc.public.tradeHistory("ltccny", limit=10)
                >>> ccs.btcc.public.tradeHistory("ltccny", since=7000)
                >>> ccs.btcc.public.tradeHistory("ltccny", since=1484396000, sincetype="time")
                >>> ccs.btcc.public.tradeHistory("ltccny", 10, 1484396000, "time")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCC]["tradeHistory"]


        .. note::
                This function use REST endpoint which is described on `Btcc-spot Trade History documentation <https://www.btcc.com/apidocs/spot-exchange-market-data-rest-api#trade-history>`_.

                Example of GET request:

                * https://data.btcchina.com/data/historydata?marktet=btccny

                * https://data.btcchina.com/data/historydata?marktet=ltccny

                * https://data.btcchina.com/data/historydata?limit=10

                * https://data.btcchina.com/data/historydata?since=5000

                * https://data.btcchina.com/data/historydata?since=5000&limit=10

                * https://data.btcchina.com/data/historydata?since=1406794449&limit=10&sincetype=time
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    if limit:
        params["limit"] = limit

    if since:
        params["since"] = since

    if sincetype:
        params["sincetype"] = sincetype

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def orderbook(market="btccny", limit=None):
    """
        This function provide lists of orders for sell and buy.

        :param String market:
                Market is currency pair.

        :param Integer limit:
                It define maximum number of asks and bids. This argument is optional.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== =============== ===================================================
                Key                 Value           Description
                =================== =============== ===================================================
                asks	            array
                bids	            array
                date	            number	        last update timestamp
                =================== =============== ===================================================

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
                >>> response = ccs.btcc.public.orderbook("btccny")
                >>> print(response)
                {
                    "asks":
                            [
                                [5721.48,0.8],
                                [5721.4,0.71],
                                ...
                            ],
                    "bids":
                            [
                                [5721,0.6097],
                                [5720.67,0.1],
                                ...
                            ],
                    "date":1484398991
                }
                >>>
                >>> # Other examples of using
                >>> ccs.btcc.public.trades("ltccny")
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCC]["trades"]


        .. note::
                This function use REST endpoint which is described on `Btcc-spot Orderbook documentation <https://www.btcc.com/apidocs/spot-exchange-market-data-rest-api#order-book>`_.

                Example of GET request:

                * https://data.btcchina.com/data/orderbook?market=btccny

                * https://data.btcchina.com/data/orderbook?market=btccny&limit=2
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    if limit:
        params["limit"] = limit

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

