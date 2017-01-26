# -*- coding: utf8 -*-

"""
This file implements classes which are object envelope for json response from requests ticker, trades, orderbook.
These classes contain json response from stock and enable unificated reading from these reponse.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

from ... import abstract
from ... import constants

#from .. import Symbol


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

# {"bids":[{"price":"752.91","amount":"9.6434","timestamp":"1480934403.0"}],"asks":[{"price":"753.61","amount":"7.9265","timestamp":"1480934404.0"}]}

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