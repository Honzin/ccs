# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Poloniex. This endpoint offer chart data.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"


import unittest
import ccs
import jsonschema
import json
import time
import datetime

def schema():
    return ccs.poloniex.configuration.SCHEMA["returnChartData"]

def sleep():
    time.sleep(3)

class Valid(unittest.TestCase):
    def setUp(self):
        self.pairs  = ["BTC_BBR", "BTC_BCN", "BTC_BELA", "BTC_BITS", "BTC_BLK", "BTC_BTCD", "BTC_BTM", "BTC_BTS", "BTC_BURST", "BTC_C2", "BTC_CLAM", "BTC_CURE"]
        self.pairs += ["BTC_DASH", "BTC_DGB", "BTC_DOGE", "BTC_EMC2", "BTC_FLDC", "BTC_FLO", "BTC_GAME", "BTC_GRC", "BTC_HUC", "BTC_HZ", "BTC_LTC", "BTC_MAID"]
        self.pairs += ["BTC_OMNI", "BTC_MYR", "BTC_NAUT", "BTC_NAV", "BTC_NEOS", "BTC_NMC", "BTC_NOBL", "BTC_NOTE", "BTC_NSR", "BTC_NXT", "BTC_PINK", "BTC_POT"]
        self.pairs += ["BTC_PPC", "BTC_QBK", "BTC_QORA", "BTC_QTL", "BTC_RBY", "BTC_RIC", "BTC_SDC", "BTC_SJCX", "BTC_STR", "BTC_SYS", "BTC_UNITY", "BTC_VIA"]
        self.pairs += ["BTC_XVC", "BTC_VRC", "BTC_VTC", "BTC_XBC", "BTC_XCP", "BTC_XEM", "BTC_XMG", "BTC_XMR", "BTC_XPM", "BTC_XRP", "USDT_BTC", "USDT_DASH"]
        self.pairs += ["USDT_LTC", "USDT_NXT", "USDT_STR", "USDT_XMR", "USDT_XRP", "XMR_BBR", "XMR_BCN", "XMR_BLK", "XMR_BTCD", "XMR_DASH", "XMR_LTC", "XMR_MAID"]
        self.pairs += ["XMR_NXT", "XMR_QORA", "BTC_IOC", "BTC_ETH", "USDT_ETH", "BTC_SC", "BTC_BCY", "BTC_EXP", "BTC_FCT", "BTC_RADS", "BTC_AMP", "BTC_VOX", "BTC_DCR"]
        self.pairs += ["BTC_LSK", "ETH_LSK", "BTC_LBC", "BTC_STEEM", "ETH_STEEM", "BTC_SBD", "BTC_ETC", "ETH_ETC", "USDT_ETC", "BTC_REP", "USDT_REP", "ETH_REP"]
        self.pairs += ["BTC_ARDR", "BTC_ZEC", "ETH_ZEC", "USDT_ZEC", "XMR_ZEC", "BTC_STRAT", "BTC_NXC"]

        self.pair = "BTC_LTC"
        sleep()

    def testSchema(self):
        s = 1410158341
        e = 1410499372
        r = ccs.poloniex.public.returnChartData(self.pair,  start=s, end=e)
        jsonschema.validate(json.loads(r), schema())


    def testStartEndPeriod(self):
        s = 1410158341
        e = 1410499372
        p = 300
        r = ccs.poloniex.public.returnChartData(self.pair, start=s, end=e, period=p)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        ds = d[0]["date"]
        de = d[-1]["date"]

        self.assertGreaterEqual(ds, s)
        self.assertLessEqual(de, e)


    @unittest.skip("time-consuming")
    def testPairs(self):
        s = 1410158341
        e = 1410499372
        for pair in self.pairs:
            r = ccs.poloniex.public.returnChartData(self.pair,  start=s, end=e)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.pair = "abcd"

    def testPair(self):
        s = 1410158341
        e = 1410499372
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.poloniex.public.returnChartData(self.pair,  start=s, end=e)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
