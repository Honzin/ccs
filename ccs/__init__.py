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

# from . import bit2c
# from . import bitbay
from . import bitfinex
# from . import bitkonan
# from . import bitmarket
# from . import bitnz
from . import bitstamp
from . import bittrex
from . import btcc
from . import btccpro
from . import btccusd
from . import btce
# from . import btcmarkets
from . import bter
from . import cexio
# from . import coinfloor
# from . import exmo
# from . import hitbtc
# from . import itbit
from . import kraken
# from . import lakebtc
# from . import localbitcoins
# from . import mercadobitcoin
from . import okcoin
from . import poloniex
# from . import therocktraiding
from . import core
from . import constants
from . import logger
from . import abstract


# from . import fybse
# from . import fybsg
from . import okcoincom
from . import okcoincn
# from . import campbx
# from . import huobi


import importlib


logger.inicialization()
cfg = core.Configuration()


def ticker(stock, cur1, cur2):
    # adapter.ticker(cur1, cur2)
    return eval(stock + ".Adapter.ticker('" + cur1 + "','" + cur2 + "')")


def trades(stock, cur1, cur2, limit=None, direction=None):
    return eval(stock + ".Adapter.trades('" + cur1 + "','" + cur2 + "')")


def orderbook(stock, cur1, cur2, limit=None):
    return eval(stock + ".Adapter.orderbook('" + cur1 + "','" + cur2 + "')")


def symbols(stock):
    return eval(stock + ".Adapter.symbols()")

def currencies(stock):
    return eval(stock + ".Adapter.currencies()")

def fees(stock):
    return eval(stock + ".Adapter.fees()")



