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
import time

from ... import abstract
from ... import constants


##################################################################################
# TICKER                                                                         #
##################################################################################

# KRAKEN
# {"error":[],"result":{"XXBTZEUR":{"a":["384.22488","1","1.000"],"b":["384.11100","1","1.000"],"c":["385.22853","0.72703961"],"v":["7657.84233459","12371.32284466"],"p":["390.44879","391.00205"],"t":[6420,11129],"l":["380.00000","380.00000"],"h":["400.00000","400.00000"],"o":"392.00000"}}}
# a = ask array(<price>, <whole lot volume>, <lot volume>),
# b = bid array(<price>, <whole lot volume>, <lot volume>),
# c = last trade closed array(<price>, <lot volume>),
# v = volume array(<today>, <last 24 hours>),
# p = volume weighted average price array(<today>, <last 24 hours>),
# t = number of trades array(<today>, <last 24 hours>),
# l = low array(<today>, <last 24 hours>),
# h = high array(<today>, <last 24 hours>),
# o = today's opening price


class Ticker(abstract.Ticker):
    def _load(self, raw):
        self._data = next(iter(json.loads(raw)["result"].values()))
        self._ts = time.time()

    def low(self):
        return float(self._data[self._mapping[constants.LOW]][1])

    def high(self):
        return float(self._data[self._mapping[constants.HIGH]][1])

    def ask(self):
        return float(self._data[self._mapping[constants.ASK]][0])

    def bid(self):
        return float(self._data[self._mapping[constants.BID]][0])

    def last(self):
        return float(self._data[self._mapping[constants.LAST]][0])

    def volume24h(self):
        return float(self._data[self._mapping[constants.VOLUME24H]][1])

    def timestamp(self):
        return self._ts


##################################################################################
# TRADES                                                                         #
##################################################################################

class Trade(abstract.Trade):
    def tid(self):
        # TODO
        return 0

    def __str__(self):
        j = {}
        for k in self._mapping:
            j[k] = self._data[self._mapping[k]]

        j[constants.SYMBOL] = self._symbol
        j[constants.STOCK] = self.stock()
        j[constants.METHOD] = self.method()
        return json.dumps(j)

# {"error":[],"result":{"XXBTZEUR":[["718.17700","0.26930000",1480922709.6833,"b","l",""],["718.33200","0.63766159",1480922720.8598,"b","l",""],["718.33300","0.02252948",1480922735.6065,"b","l",""] ...
# ... ,["718.43000","0.12956253",1480931987.3209,"b","m",""]],"last":"1480931987320941919"}}

class Trades(abstract.Trades):
    def _load(self, raw):
        self._data = json.loads(raw)["result"]
        result_keys = list(self._data)
        self._last = self._data[constants.LAST]
        symbol = [x for x in result_keys if x not in constants.LAST][0] # DANGEROUS
        self._data = self._data[symbol]

    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)


##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"error":[],"result":{"XXBTZEUR":{"asks":[["715.29800","2.050",1480934665],["715.30000","1.898",1480934665],

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order( self._data[item])

class OrderBook(abstract.OrderBook):
    def load(self, raw):
        self._data = next(iter(json.loads(raw)["result"].values()))

    def loadAsks(self):
        self._asks = Orders( self._data["asks"])

    def loadBids(self):
        self._bids = Orders( self._data["bids"])