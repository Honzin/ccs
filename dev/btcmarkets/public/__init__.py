import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response


def tick(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1.strip().upper())
    cr = cr.replace(constants.CUR2_PATTERN, cur2.strip().upper())

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def trades(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1.strip().upper())
    cr = cr.replace(constants.CUR2_PATTERN, cur2.strip().upper())


    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))

def orderbook(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1.strip().upper())
    cr = cr.replace(constants.CUR2_PATTERN, cur2.strip().upper())


    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))