import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def trades(cur1, cur2, since=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    params = {}
    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs90m
def graph90m(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs6h
def graph6h(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs1d
def graph1d(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs7d
def graph7d(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs1m
def graph1m(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs3m
def graph3m(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs6m
def graph6m(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# graphs1y
def graph1y(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    symbol = cur1.upper().strip() + cur2.upper().strip()

    # complete request
    cr = core.request(s, r).replace(constants.SYMBOL_PATTERN, symbol)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))









# IMPROVE
# CTRANSFER DODELAT NEBO NEJAK VYRESIT