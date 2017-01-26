# -*- coding: utf8 -*-

"""
This file implements functions for reading informations from Bittrex public REST endpoints.
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
# GET MARKET SUMMARY (REAL TICKER)                                               #
##################################################################################

def getMarketSummary(market):
    """
        This function provide detailed data of give market. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

        :param String market:
                Market is currency pair. For more information about markets (symbols) visit :func:`~ccs.bittrex.public.getmarkets` or :func:`~ccs.bittrex.public.getcurrencies`.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                MarketName          ?
                High                ?
                Low                 ?
                Volume              ?
                Last                ?
                BaseVolume          ?
                TimeStamp           ?
                Bid                 ?
                Ask                 ?
                OpenBuyOrders       ?
                OpenSellOrders      ?
                PrevDay             ?
                Created             ?
                DisplayMarketName   ?
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getMarketSummary("btc-ltc")
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            [
                                {
                                    "MarketName":"BTC-LTC",
                                    "High":0.00454888,
                                    "Low":0.00423000,
                                    "Volume":1598.24416057,
                                    "Last":0.00436820,
                                    "BaseVolume":6.99532215,
                                    "TimeStamp":"2017-01-08T14:17:11.43",
                                    "Bid":0.00437737,
                                    "Ask":0.00440629,
                                    "OpenBuyOrders":170,
                                    "OpenSellOrders":859,
                                    "PrevDay":0.00448802,
                                    "Created":"2014-02-13T00:00:00"
                                }
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getMarketSummary"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# GET ORDERBOOK                                                                  #
##################################################################################

def getOrderbook(market, depth=20, type="both"):
    """
        This function provide actual lists of orders for sell and buy.

        :param String market:
                Market is currency pair. For more information about markets (symbols) visit :func:`~ccs.bittrex.public.getmarkets` or :func:`~ccs.bittrex.public.getcurrencies`.

        :param Integer depth:
                It define maximum number of asks / bids. This argument is optional. Default value is 20.


                .. warning:: Depth argument is mentioned in official documentation, but server absolutely ignore this value.

        :param String type:
                This argument identify type of orderbook. Available values are:

                * sell

                * buy

                * both

                This argument is optional. Default value is "both".

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                TODO

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                Quantity
                Rate
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getOrderbook("btc-ltc")
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            {
                                "buy":
                                    [
                                        {"Quantity":0.12415465,"Rate":0.00437001},
                                        {"Quantity":3.58852516,"Rate":0.00435273},
                                        ...
                                    ],
                                "sell":
                                    [
                                        {"Quantity":41.83912609,"Rate":0.00440900},
                                        {"Quantity":2.51315302,"Rate":0.00440904},
                                        ...
                                    ]
                            }
                }
                >>>
                >>> # Other examples of using
                >>> ccs.bittrex.public.getOrderbook("btc-ltc", depth=30)
                >>> ccs.bittrex.public.getOrderbook("btc-ltc", type="sell")
                >>> ccs.bittrex.public.getOrderbook("btc-ltc", type="buy")
                >>> ccs.bittrex.public.getOrderbook("btc-ltc", depth=10, type="buy")
                >>>
                >>> # Prepared validation schema !! TYPE = BOTH
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getOrderbook"]
                >>> # Prepared validation schema !! TYPE = BUY or TYPE=SELL
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getOrderbookBuySell"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=both

                * https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=buy

                * https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=sell

                * https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=both&depth=2
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market
    if depth:
        params["depth"] = depth
    if type:
        params["type"] = type

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# GET MARKET HISTORY                                                             #
##################################################################################

def getMarketHistory(market, count=20):
    """
        This function provide history of trades.

        :param String market:
                Market is currency pair. For more information about markets (symbols) visit :func:`~ccs.bittrex.public.getmarkets` or :func:`~ccs.bittrex.public.getcurrencies`.

        :param Interger count:
                It define maximum number of trades. This argument is optional. Default value is 20. Max is 50.

                .. warning:: Count argument is mentioned in official documentation, but server absolutely ignore this value.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                TODO

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                Id
                TimeStamp
                Quantity
                Price
                Total
                FillType
                OrderType
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getMarketHistory("btc-ltc")
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            [
                                {
                                    "Id":4126151,
                                    "TimeStamp":"2017-01-09T12:32:18.377",
                                    "Quantity":66597.09000000,
                                    "Price":0.00000025,
                                    "Total":0.01664927,
                                    "FillType":"FILL",
                                    "OrderType":"BUY"
                                },
                                {
                                    "Id":4126114,
                                    "TimeStamp":"2017-01-09T12:25:54.06",
                                    "Quantity":23467.20827500,
                                    "Price":0.00000024,
                                    "Total":0.00563212,
                                    "FillType":"PARTIAL_FILL",
                                    "OrderType":"SELL"
                                }
                            ]
                }
                >>>
                >>> # Other examples of using
                >>> ccs.bittrex.public.getMarketHistory("btc-ltc", count=5)
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getMarketHistory"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-DOGE

                * https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-DOGE&count=2
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market
    if count:
        params["count"] = count
    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# GET MARKETS                                                                    #
##################################################################################

def getMarkets():
    """
        This function provide informations about available marktets.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                TODO

                ====================== ===================================================
                Key                    Description
                ====================== ===================================================
                MarketCurrency
                BaseCurrency
                MarketCurrencyLong
                BaseCurrencyLong
                MinTradeSize
                MarketName
                IsActive
                Created
                Notice
                IsSponsored
                LogoUrl
                ====================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getMarkets()
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            [
                                {
                                    "MarketCurrency":"LTC",
                                    "BaseCurrency":"BTC",
                                    "MarketCurrencyLong":"Litecoin",
                                    "BaseCurrencyLong":"Bitcoin",
                                    "MinTradeSize":0.00000001,
                                    "MarketName":"BTC-LTC",
                                    "IsActive":true,
                                    "Created":"2014-02-13T00:00:00",
                                    "Notice":null,
                                    "IsSponsored":null,
                                    "LogoUrl":"https://i.imgur.com/R29q3dD.png"
                                },
                                {
                                    "MarketCurrency":"DOGE",
                                    "BaseCurrency":"BTC",
                                    "MarketCurrencyLong":"Dogecoin",
                                    "BaseCurrencyLong":"Bitcoin",
                                    "MinTradeSize":0.00000001,
                                    "MarketName":"BTC-DOGE",
                                    "IsActive":true,
                                    "Created":"2014-02-13T00:00:00",
                                    "Notice":null,
                                    "IsSponsored":null,
                                    "LogoUrl":"https://i.imgur.com/e1RS4Hn.png"
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getMarkets"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getmarkets

    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

##################################################################################
# GET CURRENCIES                                                                 #
##################################################################################

def getCurrencies():
    """
        This function provide informations about available currencies.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                TODO

                ====================== ===================================================
                Key                    Description
                ====================== ===================================================
                Currency
                CurrencyLong
                MinConfirmation
                TxFee
                IsActive
                CoinType
                BaseAddress
                Notice
                ====================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getCurrencies()
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            [
                                {
                                    "Currency":"BTC",
                                    "CurrencyLong":"Bitcoin",
                                    "MinConfirmation":2,
                                    "TxFee":0.00020000,
                                    "IsActive":true,
                                    "CoinType":"BITCOIN",
                                    "BaseAddress":null,
                                    "Notice":null
                                },
                                {
                                    "Currency":"LTC",
                                    "CurrencyLong":"Litecoin",
                                    "MinConfirmation":6,
                                    "TxFee":0.00200000,
                                    "IsActive":true,
                                    "CoinType":"BITCOIN",
                                    "BaseAddress":null,
                                    "Notice":null
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getcurrencies"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getcurrencies

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# GET TICKER                                                                     #
##################################################################################

def getTicker(market):
    """
         This function provide tick data. This informations offer high level overview.

        :param String market:
                Market is currency pair. For more information about markets (symbols) visit :func:`~ccs.bittrex.public.getmarkets` or :func:`~ccs.bittrex.public.getcurrencies`.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                Bid
                Ask
                Last
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getTicker("btc-ltc")
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                        {
                            "Bid":0.00436403,
                            "Ask":0.00441773,
                            "Last":0.00441777
                        }
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getTicker"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getticker?market=btc-ltc
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    params["market"] = market

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

##################################################################################
# GET MARKET SUMMARIES                                                           #
##################################################################################

def getMarketSummaries():
    """
        This function provide detailed data of all markets. This informations offer high level overview of the current states on the market. It is actual price, best bids and asks etc.

        :return:
                The function return payload of http response. It is string which contains json object. Official description of keys is in the table.

                =================== ===================================================
                Key                 Description
                =================== ===================================================
                MarketName          ?
                High                ?
                Low                 ?
                Volume              ?
                Last                ?
                BaseVolume          ?
                TimeStamp           ?
                Bid                 ?
                Ask                 ?
                OpenBuyOrders       ?
                OpenSellOrders      ?
                PrevDay             ?
                Created             ?
                DisplayMarketName   ?
                =================== ===================================================

        :rtype:
                String

        :exception:
                It can raise any exception which can occur during using

                * :py:class:`http.client.HTTPSConnection`

                * :py:func:`http.client.HTTPSConnection.request`.

        :Example:
                >>> import ccs
                >>> response = ccs.bittrex.public.getMarketSummaries()
                >>> print(response)
                {
                    "success":true,
                    "message":"",
                    "result":
                            [
                                {
                                    "MarketName":"BITCNY-BTC",
                                    "High":6000.00000001,
                                    "Low":6000.00000001,
                                    "Volume":0.00000020,
                                    "Last":6000.00000001,
                                    "BaseVolume":0.00120000,
                                    "TimeStamp":"2017-01-09T13:19:54.15",
                                    "Bid":6000.00000001,
                                    "Ask":59000.00000000,
                                    "OpenBuyOrders":15,
                                    "OpenSellOrders":14,
                                    "PrevDay":6000.00000001,
                                    "Created":"2015-12-11T06:31:40.653"
                                },
                                {
                                    "MarketName":"BTC-2GIVE",
                                    "High":0.00000049,
                                    "Low":0.00000038,
                                    "Volume":36247.97622366,
                                    "Last":0.00000038,
                                    "BaseVolume":0.01447996,
                                    "TimeStamp":"2017-01-09T13:29:46.937",
                                    "Bid":0.00000039,
                                    "Ask":0.00000043,
                                    "OpenBuyOrders":52,
                                    "OpenSellOrders":394,
                                    "PrevDay":0.00000049,
                                    "Created":"2016-05-16T06:44:15.287"
                                },
                                ...
                            ]
                }
                >>>
                >>> # Prepared validation schema
                >>> schema = ccs.cfg.schema[ccs.constants.BITTREX]["getMarketSummaries"]


        .. note::
                This function use REST endpoint which is described on `Bittrex documentation <https://bittrex.com/Home/Api>`_.

                Example of GET request:

                * https://bittrex.com/api/v1.1/public/getmarketsummaries
    """

    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

