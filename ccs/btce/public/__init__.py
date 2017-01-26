# -*- coding: utf8 -*-

"""
This file implements functions for reading informations from Btce public REST endpoints.
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

def ticker(pair):
    """
        This function provide tick data. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

        :param String pair:
                For more information about symbols visit :func:`~ccs.bce.public.info`.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                high                maximum price
                low                 minimum price
                avg                 average price
                vol                 trade volume
                vol_cur             trade volume in currency
                last                the price of the last trade
                buy                 buy price
                sell                sell price
                updated             last update of cache
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btce.public.ticker("btc_usd")
                >>> print(response)
                {
                    "btc_usd":
                            {
                                "high":873,
                                "low":840,
                                "avg":856.5,
                                "vol":4891718.21757,
                                "vol_cur":5699.60085,
                                "last":860.016,
                                "buy":861.899,
                                "sell":860.001,
                                "updated":1483980795
                            }
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCE]["ticker"]


        .. note::
                This function use REST endpoint which is described on `Btce Ticker documentation <https://btc-e.com/api/3/docs#ticker>`_.

                Example of GET request:

                * https://btc-e.com/api/3/ticker/btc_usd
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, pair)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################

def trades(pair, limit=150):
    """
        This function provide history of trades.

        :param String pair:
                For more information about symbols visit :func:`~ccs.bce.public.info`.

        :param Integer limit:
                 It define maximum number of trades. This argument must be greater or equal to 1. This argument is optional. Default value is 150. Maximum is 2000.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                type                ask – sell, bid – buy.
                price               buy price or sell price.
                amount              the amount of asset bought/sold.
                tid                 trade ID.
                timestamp           Unix time of the trade.
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btce.public.trades("btc_usd")
                >>> print(response)
                {
                    "btc_usd":
                            [
                                {
                                    "type":"ask",
                                    "price":862,
                                    "amount":0.01396916,
                                    "tid":91331563,
                                    "timestamp":1483980974
                                },
                                {
                                    "type":"bid",
                                    "price":862.619,
                                    "amount":0.159,
                                    "tid":91331549,
                                    "timestamp":1483980971
                                },
                                ...
                            ]
                }
                >>>
                >>> # Other examples of using
                >>> ccs.btce.public.trades("btc_usd", limit=2)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCE]["trades"]


        .. note::
                This function use REST endpoint which is described on `Btce Trades documentation <https://btc-e.com/api/3/docs#trades>`_.

                Example of GET request:

                * https://btc-e.com/api/3/trades/btc_usd

                * https://btc-e.com/api/3/trades/btc_usd?limit=2
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if limit:
        params["limit"] = limit

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, pair) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# DEPTH                                                                          #
##################################################################################

def depth(pair, limit=150):
    """
        This function provide actual lists of orders for sell and buy.

        :param String pair:
                For more information about symbols visit :func:`~ccs.bce.public.info`.

        :param Integer limit:
                 It define maximum number of trades. This argument must be greater or equal to 1. This argument is optional. Default value is 150. Maximum is 2000.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                asks                sell orders
                bids                buy orders
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
                >>> response = ccs.btce.public.depth("btc_usd")
                >>> print(response)
                {
                    "btc_usd":
                            {
                                "asks":
                                        [
                                            [861.898,0.8],
                                            [861.899,0.00002518],
                                            ...
                                        ],
                                "bids":
                                        [
                                            [860,1.01],
                                            [859.203,0.37],
                                            ...
                                        ]
                            }
                }
                >>>
                >>> # Other examples of using
                >>> ccs.btce.public.depth("btc_usd", limit=2)
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCE]["depth"]


        .. note::
                This function use REST endpoint which is described on `Btce Depth documentation <https://btc-e.com/api/3/docs#depth>`_.

                Example of GET request:

                * https://btc-e.com/api/3/depth/btc_usd

                * https://btc-e.com/api/3/depth/btc_usd?limit=2
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if limit:
        params["limit"] = limit

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, pair) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# INFO                                                                           #
##################################################################################

def info():
    """
        This function provide all the information about currently active pairs.

        :return:
                The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                decimal_places      number of decimals allowed during trading
                min_price           minimum price allowed during trading
                max_price           maximum price allowed during trading
                min_amount          minimum sell or buy transaction size
                hidden              whether the pair is hidden, 0 or 1
                fee                 commission for this pair
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.btce.public.info()
                >>> print(response)
                {
                    "server_time":1483981601,
                    "pairs":
                            {
                                "btc_usd":
                                        {
                                            "decimal_places":3,
                                            "min_price":0.1,
                                            "max_price":10000,
                                            "min_amount":0.01,
                                            "hidden":0,
                                            "fee":0.2
                                        },
                                "btc_rur":
                                        {
                                            "decimal_places":5,
                                            "min_price":1,
                                            "max_price":1000000,
                                            "min_amount":0.01,
                                            "hidden":0,
                                            "fee":0.2
                                        },
                                        ...
                            }
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BTCE]["info"]


        .. note::
                This function use REST endpoint which is described on `Btce Info documentation <https://btc-e.com/api/3/docs#info>`_.

                Example of GET request:

                * https://btc-e.com/api/3/info
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

