import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response


def kline(cur1, cur2, period="100"):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # IMPROVE
    # strip()
    # lower()
    cur2_translation = ""
    if cur2 == "cny":
        cur2_translation = "static"

    if cur2 == "usd":
        cur2_translation = cur2

    # complete request
    cr = core.request(s, r).replace(constants.PERIOD_PATTERN, str(period))
    cr = cr.replace(constants.CUR1_PATTERN, cur1)
    cr = cr.replace(constants.CUR2_PATTERN, cur2_translation)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def ticker(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # IMPROVE
    # strip()
    # lower()
    cur2_translation = ""
    if cur2 == "cny":
        cur2_translation = "static"

    if cur2 == "usd":
        cur2_translation = cur2

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1)
    cr = cr.replace(constants.CUR2_PATTERN, cur2_translation)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))



def depth(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # IMPROVE
    # strip()
    # lower()
    cur2_translation = ""
    if cur2 == "cny":
        cur2_translation = "static"

    if cur2 == "usd":
        cur2_translation = cur2

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1)
    cr = cr.replace(constants.CUR2_PATTERN, cur2_translation)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def detail(cur1, cur2):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    # IMPROVE
    # strip()
    # lower()
    cur2_translation = ""
    if cur2 == "cny":
        cur2_translation = "static"

    if cur2 == "usd":
        cur2_translation = cur2

    # complete request
    cr = core.request(s, r).replace(constants.CUR1_PATTERN, cur1)
    cr = cr.replace(constants.CUR2_PATTERN, cur2_translation)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))