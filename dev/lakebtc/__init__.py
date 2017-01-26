from ccs import abstract
from . import configuration
from . import public


class Symbol(abstract.Symbol):
    def __init__(self, cur1, cur2):
        self._cur1 = cur1
        self._cur2 = cur2

    def cur1(self):
        return self.normalize(self._cur1)

    def cur2(self):
        return self.normalize(self._cur2)

    def normalize(self, cur):
        return cur.lower().strip()

    def __str__(self):
        return self.normalize(self._cur1) + self.normalize(self._cur2)


class Adapter(abstract.Adapter):
    @staticmethod
    def ticker(cur1, cur2):
        symbol = Symbol(cur1, cur2)
        s = str(symbol)
        return public.response.Ticker(public.ticker(s), s)

    @staticmethod
    def trades(cur1, cur2, limit=None, direction=None):
        symbol = Symbol(cur1, cur2)
        s = str(symbol)
        return public.response.Trades(public.trades(s), s)

    @staticmethod
    def orderbook(cur1, cur2, limit=None):
        symbol = Symbol(cur1, cur2)
        s = str(symbol)
        return public.response.OrderBook(public.orderbook(s), s)
