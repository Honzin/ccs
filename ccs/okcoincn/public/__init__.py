# -*- coding: utf8 -*-

"""
This file contains configuration for Okcoin.cn stock.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

import urllib.parse
import inspect

from ... import core
from ... import constants
from . import response

# !! WARN This recover response from okcoin.
# from ...okcoin.public import *

from ...okcoin.public import ticker
from ...okcoin.public import trades
from ...okcoin.public import depth
from ...okcoin.public import kline

TICKER_METHOD = inspect.getsource(ticker)
exec(TICKER_METHOD)

TRADES_METHOD = inspect.getsource(trades)
exec(TRADES_METHOD)

DEPTH_METHOD = inspect.getsource(depth)
exec(DEPTH_METHOD)

KLINE_METHOD = inspect.getsource(kline)
exec(KLINE_METHOD)

