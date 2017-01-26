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

from .constants import *


def complete(default, extension):
    for key in default:
        if key in extension:
            continue
        else:
            extension[key] = default[key]

HEADER = {'Connection': 'keep-alive',
                  'Cache-Control': 'no-cache',
                  'Accept': 'application/json',
                  'Accept-Charset': UTF8,
                  'Content-Type': 'application/x-www-form-urlencoded'}

TIMEOUT = 20

TICKER = {LOW: 'low',
          HIGH: 'high',
          ASK: 'ask',
          BID: 'bid',
          LAST: 'last',
          VOLUME24H: 'volume24h',
          TIMESTAMP: 'timestamp'}

TRADE = {TID: "tid",
         PRICE: "price",
         AMOUNT: "amount",
         TIMESTAMP: "timestamp"}

ORDER = {PRICE: "price", AMOUNT: "amount"}