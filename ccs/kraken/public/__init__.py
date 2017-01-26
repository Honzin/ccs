# -*- coding: utf8 -*-

"""
This file contains configuration for Kraken stock.
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

def getTickerInformation(pair):
    """
    This function provide tick data. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

    :param String pair:
            It is currency pair. For more information about symbols visit :func:`~ccs.kraken.public.getTradableAssetPairs`.
    :return:
            The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

            ======= ================================================================
            Key     Description
            ======= ================================================================
            a       ask array(*price*, *whole lot volume*, *lot volume*)
            b       bid array(*price*, *whole lot volume*, *lot volume*)
            c       last trade closed array(*price*, *lot volume*)
            v       volume array(*today*, *last 24 hours*),
            p       volume weighted average price array(*today*, *last 24 hours*)
            t       number of trades array(*today*, *last 24 hours*)
            l       low array(*today*, *last 24 hours*)
            h       high array(*today*, *last 24 hours*)
            o       today's opening price
            ======= ================================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getTickerInformation("XBTEUR")
            >>> print(response)
            {
                "error":[],
                "result":
                        {
                            "XXBTZEUR":
                                        {
                                            "a":["865.00000","3","3.000"],
                                            "b":["863.00000","5","5.000"],
                                            "c":["864.99900","0.39297888"],
                                            "v":["3028.35485167","13443.20773038"],
                                            "p":["871.88063","867.96689"],
                                            "t":[3160,13089],
                                            "l":["857.00000","833.94000"],
                                            "h":["888.85900","889.71200"],
                                            "o":"884.17900"
                                        }
                        }
            }
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getTickerInformation"]

    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/Ticker?pair=XBTEUR
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["pair"] = pair

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################

def getRecentTrades(pair, since=None):
    """
    This function provide history of trades.

    :param String pair:
            It is currency pair. For more information about symbols visit :func:`~ccs.kraken.public.getTradableAssetPairs`.

    :param Integer since:
            Value of since argument is trade ID. Setting this argument cause showing trades at or after the ID. This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json object with arrays. Each array describe one trade. Official description of array position is in the table.

            ========= =========================
            Position  Description
            ========= =========================
            0         price
            1         volume
            2         time
            3         buy / sell
            4         market / limit
            5         miscellaneous
            ========= =========================

            Key *last* is ID of last trade in answer from server. Note that ID can be used as since when polling for new trade data.

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getRecentTrades("XBTEUR")
            >>> print(response)
            {
                "error":[],
                "result":
                        {
                            "XXBTZEUR":
                                        [
                                            ["863.73500","0.02750313",1482576757.9252,"s","m",""],
                                            ["863.73500","4.03892266",1482576797.757,"s","l",""],
                                            ...
                                        ],
                            "last":"1482576827813240845"
                        }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getRecentTrades("XBTEUR", 1482576757925126325)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getRecentTrades"]

    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/Trades?pair=XBTEUR

            * https://api.kraken.com/0/public/Trades?pair=XBTEUR&since=1482576757925126325
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["pair"] = pair

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def getOrderBook(pair, count=None):
    """
    This function provide actual lists of orders for sell and buy.

    :param String pair:
            It is currency pair. For more information about symbols visit :func:`~ccs.kraken.public.getTradableAssetPairs`.

    :param Interger count:
            It define maximum number of asks / bids. This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json object with arrays. Each array describe one order. Official description of array position is in the table. It is same for asks and bids.

            ========= =========================
            Position  Description
            ========= =========================
            0         price
            1         volume
            2         timestamp
            ========= =========================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getOrderBook("XBTEUR")
            >>> print(response)
            {
                "error":[],
                "result":
                        {
                            "XXBTZEUR":
                                        {
                                            "asks":
                                                    [
                                                        ["863.24000","1.753",1482580426],
                                                        ["863.61000","12.500",1482579746],
                                                        ...
                                                    ],
                                            "bids":
                                                    [
                                                        ["862.00000","0.001",1482580604],
                                                        ["861.48000","3.198",1482580657],
                                                        ...
                                                    ]
                                        }
                        }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getOrderBook("XBTEUR", 3)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getOrderBook"]

    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/Depth?pair=XBTEUR

            * https://api.kraken.com/0/public/Depth?pair=XBTEUR&count=2
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["pair"] = pair

    if count:
        params["count"] = count

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADABLE ASSET PAIRS                                                           #
##################################################################################

def getTradableAssetPairs(info=None, pair=None):
    """
    This function provide detailed information about asset pairs.

    :param String info:
            This argument is optional. Possible values are in table.

            ========== =====================
            Value      Description
            ========== =====================
            info       all info (default)
            leverage   leverage info
            fees       fees schedule
            margin     margin info
            ========== =====================

    :param String pair:
            It is currency pair. This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json objects. Each object describe one pair. Official description of keys is in the table.

            =================== ====================================================================================
            Key                 Description
            =================== ====================================================================================
            altname              alternate pair name
            aclass_base          asset class of base component
            base                 asset id of base component
            aclass_quote         asset class of quote component
            quote                asset id of quote component
            lot                  volume lot size
            pair_decimals        scaling decimal places for pair
            lot_decimals         scaling decimal places for volume
            lot_multiplier       amount to multiply lot volume by to get currency volume
            leverage_buy         array of leverage amounts available when buying
            leverage_sell        array of leverage amounts available when selling
            fees                 fee schedule array in [volume, percent fee] tuples
            fees_maker           maker fee schedule array in [volume, percent fee] tuples (if on maker/taker)
            fee_volume_currency  volume discount currency
            margin_call          margin call level
            margin_stop          stop-out/liquidation margin level
            =================== ====================================================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getTradableAssetPairs()
            >>> print(response)
            {
                "error":[],
                "result":
                            {
                                "XETCXETH":
                                            {
                                                "altname":"ETCETH",
                                                "aclass_base":"currency",
                                                "base":"XETC",
                                                "aclass_quote":"currency",
                                                "quote":"XETH",
                                                "lot":"unit",
                                                "pair_decimals":8,
                                                "lot_decimals":8,
                                                "lot_multiplier":1,
                                                "leverage_buy":[2],
                                                "leverage_sell":[2],
                                                "fees":
                                                        [
                                                            [0,0.26],
                                                            [50000,0.24],
                                                            [100000,0.22],
                                                            [250000,0.2],
                                                            [500000,0.18],
                                                            [1000000,0.16],
                                                            [2500000,0.14],
                                                            [5000000,0.12],
                                                            [10000000,0.1]
                                                        ],
                                                "fees_maker":
                                                        [
                                                            [0,0.16],
                                                            [50000,0.14],
                                                            [100000,0.12],
                                                            [250000,0.1],
                                                            [500000,0.08],
                                                            [1000000,0.06],
                                                            [2500000,0.04],
                                                            [5000000,0.02],
                                                            [10000000,0]
                                                        ],
                                                "fee_volume_currency":"ZUSD",
                                                "margin_call":80,
                                                "margin_stop":40
                                            },
                                            ...
                            }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getTradableAssetPairs(info="leverage")
            >>> ccs.kraken.public.getTradableAssetPairs(info="fees")
            >>> ccs.kraken.public.getTradableAssetPairs(info="margin")
            >>> ccs.kraken.public.getTradableAssetPairs(pair="XXBTZEUR")
            >>> ccs.kraken.public.getTradableAssetPairs(pair="XXBTZEUR", info="leverage")
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getTradableAssetPairs"]

    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/AssetPairs

            * https://api.kraken.com/0/public/AssetPairs?pair=XXBTZEUR

            * https://api.kraken.com/0/public/AssetPairs?pair=XXBTZEUR&info=leverage
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if pair:
        params["pair"] = pair
    if info:
        params["info"] = info

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# SERVER TIME                                                                    #
##################################################################################

def getServerTime():
    """
    This function provide server's time.

    :return:
            The function return payload of http response. It is string which contains json object. Time is provided in two formats. First is unix timestamp and second format is correspond standard *rfc1123*.

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getServerTime()
            >>> print(response)
            {
                "error":[],
                "result":
                        {
                            "unixtime":1482674808,
                            "rfc1123":"Sun, 25 Dec 16 14:06:48 +0000"
                        }
            }
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getServerTime"]


    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/Time

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ASSET INFO                                                                     #
##################################################################################

def getAssetInfo(info=None, aclass=None, asset=None):
    """
     This function provide

    :param String info:
            This argument is optional. Possible value is only *info*. It means it is not necessary. This argument is optional.

    :param String aclass:
            It is asset class. More oficial information are missing. Try to look example for better imagination. This argument is optional.

    :param String asset:
        This information are not official. It is analogy of currency with prefix "X" and "Z" for base and quote currency (aclass). Here is possible input array. Comma delimited list of assets to get info on (default = all for given asset class) This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json objects. Each object describe one pair. Official description of keys is in the table.

            ================= ==================================================
            Key               Description
            ================= ==================================================
            altname           alternate name
            aclass            asset class
            decimals          scaling decimal places for record keeping
            display_decimals  scaling decimal places for output display
            ================= ==================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getAssetInfo()
            >>> print(response)
            {
                "error":[],
                "result":
                            {
                                "KFEE":
                                        {
                                            "aclass":"currency",
                                            "altname":"FEE",
                                            "decimals":2,
                                            "display_decimals":2
                                        },
                                "XDAO":
                                        {
                                            "aclass":"currency",
                                            "altname":"DAO",
                                            "decimals":10,
                                            "display_decimals":3
                                        },
                                        ...
                            }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getAssetInfo(aclass="currency")
            >>> ccs.kraken.public.getAssetInfo(asset="XXBT")
            >>> ccs.kraken.public.getAssetInfo(asset="XXBT,ZEUR")
            >>> ccs.kraken.public.getAssetInfo(aclss="currency", asset="XXBT")
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getAssetInfo"]


    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/Assets

            * https://api.kraken.com/0/public/Assets?asset=ZEUR

            * https://api.kraken.com/0/public/Assets?asset=ZEUR,XXBT

            * https://api.kraken.com/0/public/Assets?aclass=currency

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if info:
        params["info"] = info

    if aclass:
        params["aclass"] = aclass

    if asset:
        params["asset"] = asset

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# OHLC                                                                           #
##################################################################################

def getOHLCdata(pair, interval=None, since=None):
    """
    This function provide candlestick chart.

    :param String pair:
            It is currency pair. For more information about symbols visit :func:`~ccs.kraken.public.getTradableAssetPairs`.

    :param Integer interval:
            It is time frame interval in minutes. Possible values are 1 (default), 5, 15, 30, 60, 240, 1440, 10080, 21600.

    :param Integer since:
            Value of since argument is trade ID. Setting this argument cause showing OHLC chart at or after the ID. This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json object with arrays. Each array describe one time interval (one candle). Official description of array position is in the table.

            ========== ===============
            Position   Description
            ========== ===============
            0          time
            1          open
            2          high
            3          low
            4          close
            5          vwap
            6          volume
            7          count
            ========== ===============

            Key *last* is ID of last trade in answer from server. Note that ID can be used as since when polling for data.

            Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always be present, regardless of the value of *since*.

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getOHLCdata("XBTEUR")
            >>> print(response)
            {
                "error":[],
                "result":
                            {
                                "XXBTZEUR":
                                            [
                                                [
                                                    1482645840,
                                                    "834.000",
                                                    "834.000",
                                                    "834.000",
                                                    "834.000",
                                                    "834.000",
                                                    "0.07543179",
                                                    3
                                                ],
                                                [
                                                    1482645900,
                                                    "834.000",
                                                    "834.000",
                                                    "833.100",
                                                    "833.999",
                                                    "833.166",
                                                    "0.42388696",
                                                    5
                                                ],
                                                ...
                                            ],
                                "last":1482688920
                            }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getOHLCdata("XBTEUR", interval=5)
            >>> ccs.kraken.public.getOHLCdata("XBTEUR", since=1482689400)
            >>> ccs.kraken.public.getOHLCdata("XBTEUR", interval=5, since=1482689400)
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getOHLCdata"]


    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            * https://api.kraken.com/0/public/OHLC?pair=XBTEUR

            * https://api.kraken.com/0/public/OHLC?pair=XBTEUR&interval=5

            * https://api.kraken.com/0/public/OHLC?pair=XBTEUR&since=1482689400

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["pair"] = pair

    if interval:
        params["interval"] = interval

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# SPREAD DATA                                                                    #
##################################################################################

def getRecentSpreadData(pair, since=None):
    """
    This function provide spread data.

    :param String pair:
            It is currency pair. For more information about symbols visit :func:`~ccs.kraken.public.getTradableAssetPairs`.

    :param Integer since:
            Value of since argument is trade ID. Setting this argument cause showing spread data at or after the ID. This argument is optional.

    :return:
            The function return payload of http response. It is string which contains json object with arrays. Each array describe one time interval and its bid and ask. Official description of array position is in the table.

            ========== ===============
            Position   Description
            ========== ===============
            0          time
            1          bid
            2          ask
            ========== ===============

             Key *last* is ID of last trade in answer from server. Note that ID can be used as since when polling for data.

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.kraken.public.getRecentSpreadData("XBTEUR")
            >>> print(response)
            {
                "error":[],
                "result":
                        {
                            "XXBTZEUR":
                                        [
                                            [1482689922,"841.95000","843.00000"],
                                            [1482689932,"841.92900","843.00000"]
                                        ],
                            "last":1482690474
                        }
            }
            >>>
            >>> # Other examples of using
            >>> ccs.kraken.public.getRecentSpreadData("XBTEUR", since=1482690474)
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.KRAKEN]["getRecentSpreadData"]


    .. note::
            This function use REST endpoint which is described on `Kraken documentation <https://www.kraken.com/en-us/help/api>`_.

            Example of GET request:

            *

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["pair"] = pair

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))
