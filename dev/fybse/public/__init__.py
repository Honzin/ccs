import urllib.parse

from ccs import core
from ccs import constants
from . import response

from ...fyb.public import *
import inspect

TICKER_METHOD = inspect.getsource(ticker)
exec(TICKER_METHOD)

TICKERDETAILED_METHOD = inspect.getsource(tickerdetailed)
exec(TICKERDETAILED_METHOD)

TRADES_METHOD = inspect.getsource(trades)
exec(TRADES_METHOD)

ORDERBOOK_METHOD = inspect.getsource(orderbook)
exec(ORDERBOOK_METHOD)