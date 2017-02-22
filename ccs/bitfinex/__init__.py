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

from .. import abstract
from . import public
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
        b = r[:3]
        q = r[3:]
        return Symbol(b, q)


##################################################################################
# CURRENCY                                                                       #
##################################################################################

class Currency(abstract.Currency):
    def native(self):
        return self.c.strip().lower()


##################################################################################
# ADAPTER                                                                        #
##################################################################################

class Adapter(abstract.Adapter):
    @staticmethod
    def ticker(cur1, cur2):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.Ticker(public.ticker(s), symbol)

    @staticmethod
    def trades(cur1, cur2, limit=None, direction=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.Trades(public.trades(s), symbol)

    @staticmethod
    def orderbook(cur1, cur2, limit=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.native()
        return public.response.OrderBook(public.orderbook(s), symbol)

    @staticmethod
    def symbols():
        symbols = json.loads(public.symbols())
        r = []
        for bq in symbols:
            r.append(Symbol.split(bq))

        return r

    # TODO predelat- pouzededit z abstract. Viz abstract.Adapter
    @staticmethod
    def currencies():
        symbols = Adapter.symbols()
        r = []

        for s in symbols:
            r.append(s.base())
            r.append(s.quote())

        return set(r)


    def fees(self):
        d = {}
        d["maker"] = 0.001
        d["taker"] = 0.002

        return d
