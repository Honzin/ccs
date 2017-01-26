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
        self.ts = float(json.loads(raw)["date"])

    def timestamp(self):
        return self.ts


##################################################################################
# TRADES                                                                         #
##################################################################################

#  [{"amount":"0.123","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781524,"type":"sell"},{"amount":"0.121","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781526,"type":"sell"}

class Trade(abstract.Trade):
    pass

class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"asks":[[5308,76.65],[5307,72.487]],"bids":[[5305,32.384],[5304,397.06]]}

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order( self._data[item])

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders( self._data["asks"])

    def loadBids(self):
        self._bids = Orders( self._data["bids"])