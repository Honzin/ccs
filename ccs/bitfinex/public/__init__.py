# -*- coding: utf8 -*-

"""
This file implements functions for reading informations from Bitfinex public REST endpoints.
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
            Symbol is currency pair. For more information about symbols visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :return:
            The function return payload of http response. It is string which contains json dictionary. Official description of keys is in the table.

            ===========  ======== ===================================================
            Key          Type     Description
            ===========  ======== ===================================================
            mid          [price]  (bid + ask) / 2
            bid          [price]  Innermost bid
            ask	         [price]  Innermost ask
            last_price	 [price]  The price at which the last order executed
            low          [price]  Lowest trade price of the last 24 hours
            high         [price]  Highest trade price of the last 24 hours
            volume       [price]  Trading volume of the last 24 hours
            timestamp    [time]   The timestamp at which this information was valid
            ===========  ======== ===================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.ticker("btcusd")
            >>> print(response)
            {
                "mid":"790.395",
                "bid":"790.39",
                "ask":"790.4",
                "last_price":"790.28",
                "low":"785.59",
                "high":"792.27",
                "volume":"1684.46613188",
                "timestamp":"1482163796.189588406"
            }
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["ticker"]


    .. note::
            This function use REST endpoint which is described on `Bitfinex Ticker documentation <https://bitfinex.readme.io/reference#rest-public-ticker>`_.

            Example of GET request:

            * https://api.bitfinex.com/v1/pubticker/btcusd
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# TRADES                                                                         #
##################################################################################

def trades(symbol, timestamp=None, limit_trades=None):
    """
    This function provide history of trades.

    :param String symbol:
            Symbol is currency pair. For more information about symbols visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :param Number timestamp:
            Setting this argument cause showing trades at or after the timestamp. This argument is optional.

    :param Int limit_trades:
            It define maximum number of trades. This argument must be greater or equal to 1. This argument is optional. Default value is 50.

    :return:
            The function return payload of http response. It is string which contains json list of objects (dictionaries). One object (dictionary) represents one trade. Official description of object's keys is in the table.

            =========== ============ ==========================================
            Key	        Type	     Description
            =========== ============ ==========================================
            tid	        [integer]
            timestamp   [time]
            price       [price]
            amount      [decimal]
            exchange    [string]
            type        [string]     “sell” or “buy” (can be “” if undetermined)
            =========== ============ ==========================================


    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.
    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.trades("btcusd")
            >>> print(response)
            [
                {
                    "timestamp":1482167987,
                    "tid":25060454,
                    "price":"790.94",
                    "amount":"1.0",
                    "exchange":"bitfinex",
                    "type":"buy"
                },
                {
                    "timestamp":1482167919,
                    "tid":25060449,
                    "price":"790.89",
                    "amount":"1.0",
                    "exchange":"bitfinex",
                    "type":"buy"
                }
                ...
            ]
            >>>
            >>> # Other examples of using
            >>> ccs.bitfinex.public.trades("ltcusd", timestamp=1482185015)
            >>> ccs.bitfinex.public.trades("ltcusd", limit_trades=20)
            >>> ccs.bitfinex.public.trades("ethusd", timestamp=1482185015, limit_trades=20)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["trades"]

    .. note::
            This function use REST endpoint which is described on `Bitfinex Trades documentation <https://bitfinex.readme.io/reference#rest-public-trades>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/trades/btcusd

            * https://api.bitfinex.com/v1/trades/btcusd?limit_trades=2

            * https://api.bitfinex.com/v1/trades/btcusd?timestamp=1

            * https://api.bitfinex.com/v1/trades/btcusd?timestamp=1&limit_trades=2
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if timestamp:
        params["timestamp"] = timestamp
    if limit_trades:
        params["limit_trades"] = limit_trades

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

def orderbook(symbol, group=1, limit_bids=50, limit_asks=50):  # bool(int(group))
    """
    This function provide actual lists of orders for sell and buy.

    :param String symbol:
            Symbol is currency pair. For more information about symbols visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :param Int group:
            If value is set on 1, orders are grouped by price in the orderbook.

            If value is set on 0, orders are not grouped and sorted individually.

            This argument is optional. Default value is 1.

    :param Int limit_bids:
            It define maximum number of bids. This argument is optional. Default value is 50.

    :param Int limit_asks:
            It define maximum number of asks. This argument is optional. Default value is 50.

    :return:
            The function return payload of http response. It is string which particularly contains json with two lists of objects (dictionaries). Official description of object's keys is in the table.

            ============== ==============
            Key            Type
            ============== ==============
            price          [price]
            amount         [decimal]
            timestamp      [time]
            ============== ==============

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.orderbook("btcusd")
            >>> print(response)
            {
                "bids":
                    [
                        {
                            "price":"791.3",
                            "amount":"11.86528138",
                            "timestamp":"1482168501.0"
                        },
                        ...
                    ],
                "asks":
                    [
                        {
                            "price":"791.31",
                            "amount":"11.76087989",
                            "timestamp":"1482166207.0"
                        },
                        ...
                    ]
            }
            >>>
            >>> # Other examples of using
            >>> ccs.bitfinex.public.orderbook("ltcusd", group=0)
            >>> ccs.bitfinex.public.orderbook("ltcusd", limit_asks=2)
            >>> ccs.bitfinex.public.orderbook("ltcusd", limit_bids=2)
            >>> ccs.bitfinex.public.orderbook("ltcusd", limit_asks=2, limit_bids=2)
            >>> ccs.bitfinex.public.orderbook("ltcusd", group=0, limit_asks=2, limit_bids=2)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["orderbook"]




    .. note::
            This function use REST endpoint which is described on `Bitfinex Orderbook documentation <https://bitfinex.readme.io/reference#rest-public-orderbook>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/book/btcusd

            * https://api.bitfinex.com/v1/book/btcusd?limit_asks=2

            * https://api.bitfinex.com/v1/book/btcusd?limit_bids=2

            * https://api.bitfinex.com/v1/book/btcusd?limit_asks=2&limit_bids=2

            * https://api.bitfinex.com/v1/book/btcusd?group=0

            * https://api.bitfinex.com/v1/book/btcusd?limit_asks=2&limit_bids=2&group=0

    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if group:
        params["group"] = group
    if limit_bids:
        params["limit_bids"] = limit_bids
    if limit_asks:
        params["limit_asks"] = limit_asks

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# SYMBOLS                                                                        #
##################################################################################

def symbols():
    """
    The fucntion returns list of tradable currency pairs.

    :return:
            The function return payload of http response. It is string which contains json list of available symbols.
    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.symbols()
            >>> print(response)
            [
                "btcusd",
                "ltcusd",
                "ltcbtc",
                "ethusd",
                "ethbtc",
                "etcbtc",
                "etcusd",
                "bfxusd",
                "bfxbtc",
                "rrtusd",
                "rrtbtc",
                "zecusd",
                "zecbtc",
                "xmrusd",
                "xmrbtc"
            ]
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["symbols"]

    .. note::
            This function use REST endpoint which is described on `Bitfinex Symbols documentation <https://bitfinex.readme.io/reference#rest-public-symbols>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/symbols
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# STATS                                                                          #
##################################################################################

def stats(symbol):
    """
    The function provide statistics about symbol.

    :param String symbol:
             Symbol is currency pair. For more information about symbols visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :return:
            The function return payload of http response. It is string which contains json list of objects (dictionaries). One object (dictionary) represents statistic for period. Official description of object's keys is in the table.

            ========= ========= =========================
            Key       Type      Description
            ========= ========= =========================
            period    [integer] Period covered in days
            volume    [price]   Volume
            ========= ========= =========================

    :rtype: String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.stats("btcusd")
            >>> print(response)
            [
                {
                    "period":1,
                    "volume":"1814.47582303"
                },
                {
                    "period":7,
                    "volume":"28021.46283327"
                },
                {
                    "period":30,
                    "volume":"183014.34833507"
                }
            ]
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["stats"]

    .. note::
            This function use REST endpoint which is described on `Bitfinex Stats documentation <https://bitfinex.readme.io/reference#rest-public-stats>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/stats/btcusd
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# FUNDINGBOOK                                                                    #
##################################################################################

def fundingbook(currency, limit_bids=50, limit_asks=50):
    """
    The function provide information about full margin funding book.

    :param String currency:
        This variable will contain values like *btc*, *usd*. For more information about symbols (currencies pairs) visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :param Int limit_bids:
            It define maximum number of bids. This argument is optional. Default value is 50.

    :param Int limit_asks:
            It define maximum number of asks. This argument is optional. Default value is 50.

    :return:
            The function return payload of http response. It is string which particularly contains json with two lists of objects (dictionaries). Official description of object's keys is in the table.

            Bids

            ================= ================================== =====================================================
            Key               Type                               Description
            ================= ================================== =====================================================
            bids              [array of funding bids]
            rate              [rate in % per 365 days]
            amount            [decimal]
            period            [days]                             Minimum period for the margin funding contract
            timestamp         [time]
            frr               [yes/no]                           * **Yes** if the offer is at Flash Return Rate,
                                                                 * **No** if the offer is at fixed rate
            ================= ================================== =====================================================


            Asks


            ================= ================================== =====================================================
            Key               Type                               Description
            ================= ================================== =====================================================
            asks              [array of funding offers]
            rate              [rate in % per 365 days]
            amount            [decimal]
            period            [days]                             Maximum period for the funding contract
            timestamp         [time]
            frr               [yes/no]                           * **Yes** if the offer is at Flash Return Rate,
                                                                 * **No** if the offer is at fixed rate
            ================= ================================== =====================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.fundingbook("btc")
            >>> print(response)
            {
                "bids":[
                    {
                        "rate":"9.1287",
                        "amount":"5000.0",
                        "period":30,
                        "timestamp":"1444257541.0",
                        "frr":"No"
                    },
                    ...
                ],
                "asks":[
                    {
                        "rate":"8.3695",
                        "amount":"407.5",
                        "period":2,
                        "timestamp":"1444260343.0",
                        "frr":"No"
                    },
                    ...
                ]
            }
            >>>
            >>> # Other examples of using
            >>> ccs.bitfinex.public.fundingbook("btc", limit_asks=2)
            >>> ccs.bitfinex.public.fundingbook("btc", limit_bids=2)
            >>> ccs.bitfinex.public.fundingbook("btc", limit_asks=2, limit_bids=2)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["fundingbook"]

    .. note::
            This function use REST endpoint which is described on `Bitfinex Fundingbook documentation <https://bitfinex.readme.io/reference#rest-public-fundingbook>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/lendbook/btc

            * https://api.bitfinex.com/v1/lendbook/btc?limit_asks=1

            * https://api.bitfinex.com/v1/lendbook/btc?limit_bids=1

            * https://api.bitfinex.com/v1/lendbook/btc?limit_bids=0

            * https://api.bitfinex.com/v1/lendbook/btc?limit_asks=&limit_bids=1
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if limit_bids:
        params["limit_bids"] = limit_bids
    if limit_asks:
        params["limit_asks"] = limit_asks

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, currency) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# LENDS                                                                          #
##################################################################################

def lends(currency, timestamp=None, limit_lends=50):
    """
    The function provide a list of the most recent funding data for the given currency. It mean total amount provided and Flash Return Rate (in % by 365 days) over time.

    :param String currency:
            This variable will contain values like *btc*, *usd*. For more information about symbols (currencies pairs) visit :func:`~ccs.bitfinex.public.symbols` or :func:`~ccs.bitfinex.public.symbolsDetails`.

    :param Number timestamp:
            Setting this argument cause showing lends at or after the timestamp. This argument is optional.

    :param Int limit_lends:
            It define maximum number of lends. This argument is optional. Default value is 50.

    :return:
            The function return payload of http response. It is string which particularly contains json list of objects (dictionaries). Official description of object's keys is in the table.

            ============= ========================= ==========================================================================================
            Key           Type                      Description
            ============= ========================= ==========================================================================================
            rate          [decimal, % by 365 days]  | Average rate of total funding received at fixed
                                                    | rates, ie past Flash Return Rate annualized
            amount_lent   [decimal]                 | Total amount of open margin funding in
                                                    | the given currency
            amount_used   [decimal]                 | Total amount of open margin funding used in
                                                    | a margin position in the given currency
            timestamp     [time]
            ============= ========================= ==========================================================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.lends("btc")
            >>> print(response)
            [
                {
                    "rate":"35.6443",
                    "amount_lent":"15060.11291405",
                    "amount_used":"14766.30959039",
                    "timestamp":1482168852
                }
                ...
            ]
            >>>
            >>> # Other examples of using
            >>> ccs.bitfinex.public.lends("ltc", timestamp=1482168852)
            >>> ccs.bitfinex.public.lends("etc", limit_lends=2)
            >>> ccs.bitfinex.public.lends("btc", timestamp=1482168852, limit_lends=2)
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["lends"]


     .. note::
            This function use REST endpoint which is described on `Bitfinex Fundingbook documentation <https://bitfinex.readme.io/reference#rest-public-fundingbook>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/lends/btc

            * https://api.bitfinex.com/v1/lends/btc?limit_lends=2

            * https://api.bitfinex.com/v1/lends/btc?timestamp=1482000000

            * https://api.bitfinex.com/v1/lends/btc?timestamp=1482000000&limit_lends=2
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    params = {}
    if timestamp:
        params["timestamp"] = timestamp
    if limit_lends:
        params["limit_lends"] = limit_lends

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, currency) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


##################################################################################
# SYMBOLSBETAILS                                                                 #
##################################################################################

def symbolsDetails():
    """
    The function returns information about traidable pairs.

    :return:
            The function return payload of http response. It is string which particularly contains json list of objects (dictionaries). Official description of object's keys is in the table.

            ==================== =============== ====================================================================
            Key                  Type            Description
            ==================== =============== ====================================================================
            pair                 [string]        The pair code
            price_precision      [integer]       Maximum number of significant digits for price in this pair
            initial_margin	     [decimal]       Initial margin required to open a position in this pair
            minimum_margin	     [decimal]       Minimal margin to maintain (in %)
            maximum_order_size	 [decimal]       Maximum order size of the pair
            expiration	         [string]        Expiration date for limited contracts/pairs
            ==================== =============== ====================================================================

    :rtype:
            String

    :exception:
            It can raise any exception which can occur during using

            * :py:class:`http.client.HTTPSConnection`

            * :py:func:`http.client.HTTPSConnection.request`.

    :Example:
            >>> import ccs
            >>> response = ccs.bitfinex.public.symbolsDetails()
            >>> print(response)
            [
                {
                    "pair":"btcusd",
                    "price_precision":5,
                    "initial_margin":"30.0",
                    "minimum_margin":"15.0",
                    "maximum_order_size":"2000.0",
                    "minimum_order_size":"0.01",
                    "expiration":"NA"
                }
                ...
            ]
            >>>
            >>> # Prepared validation schema
            >>> schema = ccs.cfg.schema[ccs.constants.BITFINEX]["symbolsDetails"]

    .. note::
            This function use REST endpoint which is described on `Bitfinex Fundingbook documentation <https://bitfinex.readme.io/reference#rest-public-fundingbook>`_.

            Examples of GET request:

            * https://api.bitfinex.com/v1/symbols_details
    """
    s = __name__.split(".")[1]  # stock name
    r = sys._getframe().f_code.co_name  # request name is same as name of function

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


