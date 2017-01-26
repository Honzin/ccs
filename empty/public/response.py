from ... import abstract
from ... import constants


##################################################################################
# TICKER                                                                         #
##################################################################################

class Ticker(abstract.Ticker):
    pass


##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    pass

class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order(self._data[item])

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders(self._data["asks"])

    def loadBids(self):
        self._bids = Orders(self._data["bids"])