import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def ticker(currency):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    c = ""
    if currency == constants.BTC:
        c = ""

    if currency == constants.LTC:
        c = "_litecoin"

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, c)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def trades(currency, tid=None, since=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    c = ""
    if currency == constants.BTC:
        c = ""

    if currency == constants.LTC:
        c = "_litecoin"

    # IMPROVE
    # viz dokumentace
    # nelze kombinovat since & tid
    # neni to uplne jeste je mozne nastavovat time_inicial ...
    params = {}
    if tid:
        params["tid"] = tid

    if since:
        params["since"] = since

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, c) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))



def orderbook(currency):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    c = ""
    if currency == constants.BTC:
        c = ""

    if currency == constants.LTC:
        c = "_litecoin"

    # complete request
    cr = core.request(s, r).replace(constants.CURRENCY_PATTERN, c)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))