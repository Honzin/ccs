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
import datetime

from ... import abstract
from ... import constants


##################################################################################
# TICKER                                                                         #
##################################################################################

class Ticker(abstract.Ticker):
    def _load(self, raw):
        # TODO - symbol
        self._data = json.loads(raw)[self.osymbol()]
        self._ts = time.time()

    def timestamp(self):
        return self._ts



##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    def timestamp(self):
        return datetime.datetime.strptime(self._data[self._mapping[constants.TIMESTAMP]], "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()

# [{"globalTradeID":68172545,"tradeID":2209360,"date":"2016-12-07 17:12:17","type":"sell","rate":"0.00470928","amount":"0.03746884","total":"0.00017645"},
# {"globalTradeID":68172456,"tradeID":2209359,"date":"2016-12-07 17:11:43","type":"sell","rate":"0.00470926","amount":"0.02237958","total":"0.00010539"}]

class Trades(abstract.Trades):
    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"asks":[["0.00000835",200000],["0.00000836",73693]],"bids":[["0.00000830",764.37447053],["0.00000829",42.40070418]],"isFrozen":"0","seq":20303134}

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