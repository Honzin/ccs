import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response


def tickers():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def trades(currency):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, currency)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(currency):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, currency)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))