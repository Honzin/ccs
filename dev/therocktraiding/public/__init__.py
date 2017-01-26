import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker(id):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, id)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def tickers():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def trades(id):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, id)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(id):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, id)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def fund(id):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, id)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def funds():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))