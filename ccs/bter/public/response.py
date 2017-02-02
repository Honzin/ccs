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


import time
import json

from ... import abstract
from ... import constants


##################################################################################
# TICKER                                                                         #
##################################################################################

class Ticker(abstract.Ticker):
    def _load(self, raw):
        self._data = json.loads(raw)
        self._ts = time.time()

    def volume24h(self):
        # TODO vol_btc, vol_cny ...
        return 0

    def timestamp(self):
        return self._ts

##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    pass

# {"result":"true","data":[{"date":"1481128134","price":5323.44,"amount":0.004,"tid":"351129","type":"sell"},{"date":"1481128141","price":5323.61,"amount":0.028,"tid":"351130","type":"sell"}],"elapsed":"0.089ms"}

class Trades(abstract.Trades):
    def _load(self, raw):
        self._data = json.loads(raw)["data"]

    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

#{"result":"true","asks":[[5349.99,0.5],[5349,5.543],[5345.27,5],[5345,0.297],[5340,0.138],[5338,0.03],[5336.5,0.18],[5329.35,0.081]],
# "bids":[[5327.63,0.5],[5327.11,0.086],[5326.82,0.029],[5288.05,0.513],[5288,29.98],[5285,0.165]]}

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order(self._data[item], self._symbol)

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders(self._data["asks"], self._symbol)

    def loadBids(self):
        self._bids = Orders(self._data["bids"], self._symbol)