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


import json

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

# [{"date": "1480928480", "tid": 12584559, "price": "749.26", "type": 1, "amount": "0.00665990"}, {"date": "1480928462", "tid": 12584558, "price": "749.18", "type": 0, "amount": "0.45830000"}]
class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)




##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"timestamp": "1480934398", "bids": [["748.89", "22.60247740"], ["748.00", "34.43100000"], ["747.99", "8.08296501"], ["747.98", "20.00000000"],

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