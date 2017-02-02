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

from . import public
from .. import abstract

# "btc_cny"

class Symbol(abstract.Symbol):
    def original(self):
        return self.normalize(self._cur1) + '_' + self.normalize(self._cur2)


class Adapter(abstract.Adapter):
    @staticmethod
    def ticker(cur1, cur2):
        symbol = Symbol(cur1, cur2)
        s = symbol.original()
        return public.response.Ticker(public.ticker(s), symbol)

    @staticmethod
    def trades(cur1, cur2, limit=None, direction=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.original()
        return public.response.Trades(public.tradeHistory(s), symbol)

    @staticmethod
    def orderbook(cur1, cur2, limit=None):
        symbol = Symbol(cur1, cur2)
        s = symbol.original()
        return public.response.OrderBook(public.depth(s), symbol)


# class Handler(abstract.Handler):
#     def _setAdapter(self):
#         self._adapter = Adapter()
