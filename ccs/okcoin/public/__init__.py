# -*- coding: utf8 -*-

"""
This file contains configuration for Okcoin stock.
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

            =================== ===================================================
            Key                 Description
            =================== ===================================================
            date                server time for returned data
            buy                 best bid
            high                highest price
            last                latest price
            low                 lowest price
            sell                best ask
            vol                 volume (in the last rolling 24 hours)
            =================== ===================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.okcoincom.public.ticker("btc_usd")
            >>> print(response)
            {
                "date":"1483982377",
                "ticker":
                        {
                            "buy":"893.01",
                            "high":"912.0",
                            "last":"894.0",
                            "low":"862.91",
                            "sell":"893.91",
                            "vol":"2340.0015"
                        }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.okcoincn.public.ticker("btc_cny")
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCOM]["ticker"]
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCN]["ticker"]


    .. note::
            This function use REST endpoint which is described on `Okcoin documentation <https://www.okcoin.com/rest_api.html>`_.

            Example of GET request:

            * https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd

            * https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd

            * https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny

            * https://www.okcoin.cn/api/v1/ticker.do?symbol=ltc_cny
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # TODO
    ## zkontrolovat dokumentaci
    params = {}
    if symbol:
        params["symbol"] = symbol

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    # return core.get(core.hostname(s) + domain(symbol), cr, core.header(s), core.compression(s), core.timeout(s))
    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################
# TODO Formatovani v html je spatne

def trades(symbol, since=1):
    """
       This function provide history of trades.

        :param String symbol:
                Symbol is currency pair.

        :param Integer since:
                Get recently 600 pieces of data starting from the given tid (optional).

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                date                transaction time
                date_ms             transaction time in milliseconds
                price               transaction price
                amount              quantity in BTC (or LTC)
                tid                 transaction ID
                type                buy/sell
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.okcoincom.public.trades("btc_usd")
                >>> print(response)
                [
                    {
                        "amount":"0.099",
                        "date":1483981229,
                        "date_ms":1483981229000,
                        "price":"887.22",
                        "tid":208393434,
                        "type":"sell"
                    },
                    {
                        "amount":"0.705",
                        "date":1483981229,
                        "date_ms":1483981229000,
                        "price":"887.01",
                        "tid":208393436,
                        "type":"sell"
                    },
                    ...
                ]
                >>>
                >>> # Other examples of using
                >>> ccs.okcoincn.public.trades("btc_cny")
                >>> ccs.okcoincom.public.trades("ltc_usd", since=150)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCOM]["trades"]
                >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCN]["trades"]


        .. note::
                This function use REST endpoint which is described on `Okcoin documentation <https://www.okcoin.com/rest_api.html>`_.

                Example of GET request:

                * https://www.okcoin.com/api/v1/trades.do?symbol=btc_usd

                * https://www.okcoin.com/api/v1/trades.do?symbol=ltc_usd

                * https://www.okcoin.cn/api/v1/trades.do?symbol=btc_cny

                * https://www.okcoin.cn/api/v1/trades.do?symbol=ltc_cny
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # TODO
    ## zkontrolovat dokumentaci
    params = {}
    if symbol:
        params["symbol"] = symbol

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    # return core.get(core.hostname(s) + domain(symbol), cr, core.header(s), core.compression(s), core.timeout(s))
    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def depth(symbol, size=None, merge=1):
    """
    This function provide actual lists of orders for sell and buy.

    :param String symbol:
            Symbol is currency pair.

    :param Integer size:
            TODO value: must be between 1 - 200

    :param Integer merge:
            TODO value: 1, 0.1 (merge depth)

    :return:
            The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

            =================== ===================================================
            Key                 Description
            =================== ===================================================
            asks                ask depth
            bids                bid depth
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
            >>> response = ccs.okcoincom.public.depth("btc_usd")
            >>> print(response)
            {
                "asks":
                    [
                        [930.03,3],
                        [930,0.47],
                        ...
                    ],
                "bids":
                    [
                        [889.24,0.284],
                        [889.02,0.336],
                        ...
                    ]
            }
            >>>
            >>> # Other examples of using
            >>> ccs.okcoincn.public.depth("btc_cny")
            >>> ccs.okcoincom.public.depth("btc_usd", size=2)
            >>> ccs.okcoincom.public.depth("btc_usd", merge=1)
            >>> ccs.okcoincom.public.depth("btc_usd", size=2, merge=1)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCOM]["depth"]
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCN]["depth"]


    .. note::
            This function use REST endpoint which is described on `Okcoin documentation <https://www.okcoin.com/rest_api.html>`_.

            Example of GET request:

            * https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd

            * https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=2

            * https://www.okcoin.com/api/v1/depth.do?symbol=btc_usd&size=2&merge=1
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # TODO
    ## zkontrolovat dokumentaci
    params = {}
    if symbol:
        params["symbol"] = symbol

    if size:
        params["size"] = size

    if merge:
        params["merge"] = merge

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    # return core.get(core.hostname(s) + domain(symbol), cr, core.header(s), core.compression(s), core.timeout(s))
    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# KLINE                                                                          #
##################################################################################

# TODO
def kline():
    """
    This function provide candlestick Data.

    :return:
            The function return payload of http response. It is string which contains json array. Each item in arrays describes one candle. Official description of array position is in the table.

            ========= =========================
            Position  Description
            ========= =========================
            0         timestamp
            1         open
            2         high
            3         low
            4         close
            5         volume
            ========= =========================

    :rtype:
            String

    .. warning:: This function doesnt work.

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.okcoincom.public.kline()
            >>> print(response)
            [
                [
                    1417478400000,
                    380.94,
                    387.7,
                    378.75,
                    384.61,
                    6857.31
                ],
                [
                    1417564800000,
                    384.47,
                    387.13,
                    383.5,
                    387.13,
                    1062.04
                ]
            ]
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCOM]["kline"]
            >>> schema = ccs.cfg.schema[ccs.constants.OKCOINCN]["kline"]


    .. note::
            This function use REST endpoint which is described on `Okcoin documentation <https://www.okcoin.com/rest_api.html>`_.

            Example of GET request:

            * https://www.okcoin.com/api/v1/kline.do
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    # return core.get(core.hostname(s) + domain(""), cr, core.header(s), core.compression(s), core.timeout(s))
    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))