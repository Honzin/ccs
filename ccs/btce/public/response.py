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
        self._data = next(iter(json.loads(raw).values()))


##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    pass


#{"btc_usd":[{"type":"ask","price":753,"amount":0.133,"tid":88349995,"timestamp":1480931524},{"type":"ask","price":753,"amount":0.101,"tid":88349992,"timestamp":1480931522}]}
class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)

    def _load(self, raw):
        self._data = next(iter(json.loads(raw).values()))



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"btc_usd":{"asks":[[754.237,1.3147],[754.239,1.3142]],"bids":[[754.01,3.99540232],[754,16.99698866]]}}

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order( self._data[item])

class OrderBook(abstract.OrderBook):
    def load(self, raw):
        self._data = next(iter(json.loads(raw).values()))

    def loadAsks(self):
        self._asks = Orders( self._data["asks"])

    def loadBids(self):
        self._bids = Orders( self._data["bids"])