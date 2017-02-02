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

# [{"type":"buy","date":"1405872964","amount":"0.05985928","price":"613.00000000","tid":"1000"},{"type":"buy","date":"1405872964","amount":"0.00064442","price":"612.99200000","tid":"999"}]

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
        return Order( self._data[item], self._symbol)

class OrderBook(abstract.OrderBook):
    def loadAsks(self):
        self._asks = Orders( self._data["asks"], self._symbol)

    def loadBids(self):
        self._bids = Orders( self._data["bids"], self._symbol)