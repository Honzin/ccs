# -*- coding: utf8 -*-

# TODO
"""
...
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
import logging
import datetime
import inspect
import sys
import jsonschema

from . import constants
from . import initials
from . import core

##################################################################################
# BASE                                                                           #
##################################################################################

class Base:
    """
    Base like hell
    """
    def stock(self):
        """
        Stock like hell
        :return:
        """
        return type(self).__module__.split(".")[1]

    def method(self):
        return self.__class__.__name__.lower()

    def osymbol(self):
        if self._symbol:
            return self._symbol.original()
        else:
            return ""

    def usymbol(self):
        if self._symbol:
            return self._symbol.unificated()
        else:
            return ""

    def _save(self, raw):
        # TODO
        # volat tuhle metodu neni efektivni
        # udelat pres self.cfg
        if core.raw():
            self._raw = raw
        else:
            self._raw = ""

    def raw(self):
        return self._raw

    def data(self):
        return self._data

    def valid(self, raw):
        schema = self._cfg.schema[self.stock()][constants.UNIFICATED + "_" + self.method()]
        jsonschema.validate(json.loads(raw), schema)

    def timestamp(self):
        pass

    def dt(self, tz=None):
        pass

    def utc(self):
        return datetime.datetime.utcfromtimestamp(self.timestamp())

##################################################################################
# TICKER                                                                         #
##################################################################################

class Ticker(Base):
    """
    Ticker like hell
    """
    def __init__(self, raw, symbol=None):
        self._cfg = core.Configuration()
        self.valid(raw)
        self._symbol = symbol
        self._save(raw)
        self._load(raw)
        self._mapping = self._cfg.mapping[self.stock()][self.method()]

    def _load(self, raw):
        self._data = json.loads(raw)

    # def method(self):
    #     return self.__class__.__name__.lower()

    # def symbol(self):
    #     return self._symbol

    # def _save(self, raw):
    #     if core.raw():
    #         self._raw = raw
    #     else:
    #         self._raw = ""


    def low(self):
        """
        Low like hell
        :return:
        """
        return float(self._data[self._mapping[constants.LOW]])

    def high(self):
        return float(self._data[self._mapping[constants.HIGH]])

    def ask(self):
        return float(self._data[self._mapping[constants.ASK]])

    def bid(self):
        return float(self._data[self._mapping[constants.BID]])

    def last(self):
        return float(self._data[self._mapping[constants.LAST]])

    def volume24h(self):
        return float(self._data[self._mapping[constants.VOLUME24H]])

    def timestamp(self):
        return float(self._data[self._mapping[constants.TIMESTAMP]])

    def dt(self, tz=None):
        return datetime.datetime.fromtimestamp(self.timestamp(), tz=tz)

    def spread(self):
        return ((self.ask() - self.bid()) / self.ask()) * 100

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    # def raw(self):
    #     return self._raw

    def __str__(self):
        # TODO
        # revers atp neni potreba
        revers = {v: k for k, v in self._mapping.items()}
        j = {v: getattr(self, v)() for k, v in revers.items()}
        j[constants.OSYMBOL] = self.osymbol()
        j[constants.USYMBOL] = self.usymbol()
        j[constants.STOCK] = self.stock()
        j[constants.METHOD] = self.method()
        return json.dumps(j)

    # def data(self):
    #     return self._data

    # def valid(self):
    #     schema = self._cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._data, schema)

##################################################################################
# TRADES                                                                         #
##################################################################################

class Trades(Base):
    # REVERSE
    def __init__(self, raw, symbol=None):
        self._cfg = core.Configuration()
        self.valid(raw)
        self._save(raw)
        self._load(raw)
        self._count = len(self._data)
        self._symbol = symbol
        # TODO
        self._a = json.loads(raw)
        #self.mapping = self.cfg.mapping[self.stock][self.type]

    def _load(self, raw):
        self._data = json.loads(raw)

    # def method(self):
    #     return self.__class__.__name__.lower()

    # def _save(self, raw):
    #     if core.raw():
    #         self._raw = raw

    def __len__(self):
        return self._count

    def __getitem__(self, item):
        return Trade(self._data[item], self._symbol)

    def __str__(self):
        s = ""
        for t in self:
            s += str(t) + "\n"
        return s

    # def source(self):
    #     return self._data

    # def raw(self):
    #     return self._raw

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    # def valid(self):
    #     schema = self.cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._a, schema)

##################################################################################
# TRADE                                                                          #
##################################################################################

class Trade(Base):
    def __init__(self, data, symbol=None):
        self._cfg = core.Configuration()
        self._load(data)
        self._symbol = symbol
        self._mapping = self._cfg.mapping[self.stock()][self.method()]
        self._type_mapping = self._cfg.mapping[self.stock()][constants.TRADE_TYPE]

    def _load(self, data):
        self._data = data

    # def method(self):
    #     return self.__class__.__name__.lower()

    def tid(self):
        return float(self._data[self._mapping[constants.TID]])

    def price(self):
        return float(self._data[self._mapping[constants.PRICE]])

    def amount(self):
        return float(self._data[self._mapping[constants.AMOUNT]])

    def _normalization(self, t):
        if str(t) == str(self._type_mapping[constants.BUY]):
            return constants.BUY
        if str(t) == str(self._type_mapping[constants.SELL]):
            return constants.SELL
        return constants.UNDEFINED

    def type(self):
        return self._normalization(self._data[self._mapping[constants.TYPE]])

    def timestamp(self):
        return float(self._data[self._mapping[constants.TIMESTAMP]])

    def dt(self, tz=None):
        return datetime.datetime.fromtimestamp(self.timestamp(), tz=tz)

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    def __str__(self):
        # TODO
        # ctypes Method
        revers = {v: k for k, v in self._mapping.items()}
        j = {v: getattr(self, v)() for k, v in revers.items()}
        #j[constants.SYMBOL] = self._symbol
        j[constants.STOCK] = self.stock()
        j[constants.METHOD] = self.method()
        return json.dumps(j)

    # def valid(self):
    #     schema = self.cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._data, schema)


##################################################################################
# ORDER                                                                          #
##################################################################################


class Order(Base):
    def __init__(self, data, symbol=None):
        self._cfg = core.Configuration()
        self.load(data)
        self._symbol = symbol
        self._mapping = self._cfg.mapping[self.stock()][self.method()]

    # def method(self):
    #     return self.__class__.__name__.lower()

    def load(self, data):
        self._data = data

    def price(self):
        return float(self._data[self._mapping[constants.PRICE]])

    def amount(self):
        return float(self._data[self._mapping[constants.AMOUNT]])

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    def __str__(self):
        # TODO
        return constants.PRICE + ": " + str(self.price()) + ", " + constants.AMOUNT + ": " + str(self.amount())

    # def valid(self):
    #     schema = self.cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._data, schema)



##################################################################################
# ORDERS                                                                         #
##################################################################################

class Orders(Base):
    def __init__(self, data, symbol=None):
        # IMRPOVE
        # zvazit jestli to chci pro vsechny nebo staci jen nekde
        self._cfg = core.Configuration()
        self.load(data)
        self._symbol = symbol

    def load(self, data):
        self._data = data

    # def method(self):
    #     return self.__class__.__name__.lower()

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    def __getitem__(self, item):
        return Order(self._data[item], self._symbol)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        # TODO
        # stejne pro trades !
        s = ""
        for o in self:
            s += str(o) + "\n"
        return s

    # def valid(self):
    #     schema = self.cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._data, schema)

##################################################################################
# ORDERBOOK                                                                      #
##################################################################################

class OrderBook(Base):
    # REVERSE
    def __init__(self, raw, symbol=None):
        self._cfg = core.Configuration()
        self.valid(raw)
        self._symbol = symbol
        self._save(raw)
        self.load(raw)
        self.loadAsks()
        self.loadBids()
        # TODO
        #self._a = json.loads(raw)
        #self._type = constants.ORDER
        # self._mapping = self.cfg.mapping[self._stock][self._type]

    def load(self, raw):
        self._data = json.loads(raw)

    # def method(self):
    #     return self.__class__.__name__.lower()

    def loadAsks(self):
        self._asks = Orders(self._data["asks"], self._symbol)

    def loadBids(self):
        self._bids = Orders(self._data["bids"], self._symbol)

    # def saveraw(self, raw):
    #     if core.raw():
    #         self._raw = raw

    def asks(self):
        return self._asks

    def bids(self):
        return self._bids

    # def stock(self):
    #     return type(self).__module__.split(".")[1]

    def __str__(self):
        # TODO
        # JSON
        s = "ASKS" + "\n"
        s += str(self._asks)
        s += "BIDS" + "\n"
        s += str(self._bids)
        return s

    # def valid(self):
    #     schema = self.cfg.schema[self.stock()][self.method()]
    #     jsonschema.validate(self._a, schema)


##################################################################################
# SYMBOL                                                                         #
##################################################################################

class Symbol:
    def __init__(self, cur1, cur2):
        self._cur1 = cur1
        self._cur2 = cur2

    def cur1(self):
        return self.normalize(self._cur1)

    def cur2(self):
        return self.normalize(self._cur2)

    def normalize(self, cur):
        return cur.lower().strip()

    def original(self):
        pass

    def unificated(self):
        return self.normalize(self._cur1) + ":" + self.normalize(self._cur2)

    def __str__(self):
        pass


##################################################################################
# ADAPTER                                                                        #
##################################################################################

class Adapter:
    @staticmethod
    def ticker(cur1, cur2):
        pass

    @staticmethod
    def trades(cur1, cur2, limit=None, direction=None):
        pass

    @staticmethod
    def orderbook(cur1, cur2, limit=None):
        pass

    @staticmethod
    def symbols(stock):
        pass

    @staticmethod
    def currencies(stock):
        pass
