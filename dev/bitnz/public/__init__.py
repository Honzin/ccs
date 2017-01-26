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

def trades():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

# nejaky problem s kodovanim
# def trades_chart():
#     s = __name__.split(".")[1]
#     r = sys._getframe().f_code.co_name
#
#     # complete request
#     cr = core.request(s, r)
#
#     return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook():
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))