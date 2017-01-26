import urllib.parse
import sys

from ccs import core
from ccs import constants
from . import response

def xticker(callback=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    params = {}
    if callback:
        params["callback"] = callback

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))


def xdepth(callback=None):
    s = __name__.split(".")[1]
    r = sys._getframe().f_code.co_name

    params = {}
    if callback:
        params["callback"] = callback

    # complete request
    cr = core.request(s, r) + urllib.parse.urlencode(params)

    return core.get(core.hostname(s), cr, core.header(s), core.compression(s), core.timeout(s))