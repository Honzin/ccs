# -*- coding: utf8 -*-

"""
This file implementns:

* class adapter which offer unificated API for requests ticker, trades, orderbook, ...

* class for symbol
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

import json

from . import public
from .. import abstract
from . import configuration


##################################################################################
# SYMBOL                                                                         #
##################################################################################

class Symbol(abstract.Symbol):
    def __init__(self, base, quote):
        self._base  = Currency(base)
        self._quote = Currency(quote)

    def native(self):
        return self.base().native() + self.quote().native()

    @staticmethod
    def split(basequote):
        r = basequote.strip()
        sep = 0
        if len(r) == 6:
            sep = 3
        else:
            sep = 4
        b = r[:sep]
        q = r[sep:]
        return Symbol(b, q)


##################################################################################
# CURRENCY                                                                       #
##################################################################################

class Currency(abstract.Currency):
    def unificated(self):
        # Using Altname
        c = self.c.strip().lower()
        if c == "xxbt" or c == "xbt":
            c = "btc"
        if len(c) == 3:
            return c
        else:
            return c[1:]

    def native(self):
        # Using Altname
        c = self.c.strip().upper()
        if c == "BTC":
            c = "XBT"
        if len(c) == 3:
            return c
        else:
            return c[1:]


##################################################################################
# ADAPTER                                                                        #
##################################################################################

class Adapter(abstract.Adapter):
    @staticmethod
    def ticker(cur1, cur2):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.Ticker(public.getTickerInformation(s), symbol)

    @staticmethod
    def trades(cur1, cur2, limit=None, direction=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.Trades(public.getRecentTrades(s), symbol)

    @staticmethod
    def orderbook(cur1, cur2, limit=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.OrderBook(public.getOrderBook(s), symbol)


    @staticmethod
    def symbols():
        pairs = json.loads(public.getTradableAssetPairs())["result"]
        r = []

        for pair in pairs:
            # b = pairs[pair]["base"]
            # q = pairs[pair]["quote"]
            alt = pairs[pair]["altname"]
            if ".d" not in alt and ".d" not in pair:
                r.append(Symbol.split(alt))

        return r

    # TODO predelat - pouzededit z abstract. Viz abstract.Adapter
    @staticmethod
    def currencies():
        symbols = Adapter.symbols()
        r = []

        for s in symbols:
            r.append(s.base())
            r.append(s.quote())

        return set(r)
