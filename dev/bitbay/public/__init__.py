import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker(cur1, cur2=constants.USD):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def trades(cur1, cur2=constants.USD, since=None, sort=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + cur2

    # sort =
    # "desc" - returns the transactions in the order of newest to oldest
    # "asc"  - for the return transaction in reverse

    params = {}

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(cur1, cur2=constants.USD):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def market(cur1, cur2=constants.USD):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def all(cur1, cur2=constants.USD):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1 + cur2

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))