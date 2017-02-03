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
    def _load(self, raw):
        self._data = json.loads(raw)["ticker"]

    def timestamp(self):
        return float(str(self._data[self._mapping[constants.TIMESTAMP]])[:-3])


##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    def timestamp(self):
        return float(str(self._data[self._mapping[constants.TIMESTAMP]])[:-3])


# [{"date":"1480926246","price":5336.46,"amount":0.15,"tid":"104899229"},{"date":"1480926247","price":5336.53,"amount":11,"tid":"104899230"}]
class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"asks":[[5308,2],[5307.9,0.2621]],"bids":[[5307.24,0.0539],[5307.01,0.0152]],"date":1480934406}

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order( self._data[item], self._symbol)

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders( self._data["asks"], self._symbol)

    def loadBids(self):
        self._bids = Orders( self._data["bids"], self._symbol)