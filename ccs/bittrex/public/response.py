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



import datetime
import json

from ... import abstract
from ... import constants


##################################################################################
# TICKER                                                                         #
##################################################################################

class Ticker(abstract.Ticker):
    def _load(self, raw):
        self._data = next(iter(json.loads(raw)["result"]))

    def timestamp(self):
        return datetime.datetime.strptime(self._data[self._mapping[constants.TIMESTAMP]], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=datetime.timezone.utc).timestamp()


##################################################################################
# TRADES                                                                         #
##################################################################################

# {"success":true,"message":"","result":[{"Id":3937197,"TimeStamp":"2016-12-07T16:38:09.407","Quantity":25682.95434300,"Price":0.00000028,"Total":0.00719122,"FillType":"FILL","OrderType":"BUY"},
# {"Id":3937196,"TimeStamp":"2016-12-07T16:38:09.407","Quantity":70042.99000000,"Price":0.00000028,"Total":0.01961203,"FillType":"PARTIAL_FILL","OrderType":"BUY"}]}


class Trade(abstract.Trade):
    def timestamp(self):
        return datetime.datetime.strptime(self._data[self._mapping[constants.TIMESTAMP]], "%Y-%m-%dT%H:%M:%S.%f").replace(tzinfo=datetime.timezone.utc).timestamp()

class Trades(abstract.Trades):
    def _load(self, raw):
        self._data = json.loads(raw)["result"]

    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)



##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

# {"success":true,"message":"","result":{"buy":[{"Quantity":6.87380996,"Rate":0.00483245},{"Quantity":11.17963560,"Rate":0.00483230}],
# "sell":[{"Quantity":200.00000000,"Rate":0.00487650},{"Quantity":26.10300000,"Rate":0.00488824}]}}

class Order(abstract.Order):
    pass

class Orders(abstract.Orders):
    def __getitem__(self, item):
        return Order(self._data[item], self._symbol)

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders(self._data["result"][self._cfg.mapping[self.stock()][self.method()][constants.ASKS]], self._symbol)

    def loadBids(self):
        self._bids = Orders(self._data["result"][self._cfg.mapping[self.stock()][self.method()][constants.ASKS]], self._symbol)