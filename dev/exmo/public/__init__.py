import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def trades(pair):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    params = {}
    params["pair"] = pair

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def order_book(pair, limit=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    params = {}
    params["pair"] = pair

    if limit:
        params["limit"] = limit

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def pair_settings():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def currency():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))