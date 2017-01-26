import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response


def ticker(symbol):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def trades(symbol):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(symbol):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def recenttrades():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def time():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def symbols():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))