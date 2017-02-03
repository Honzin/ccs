# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Poloniex. This endpoint offer informations about loans.
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
    return ccs.poloniex.configuration.SCHEMA["returnLoanOrders"]

def sleep():
    time.sleep(3)

class Valid(unittest.TestCase):
    def setUp(self):
        self.currencies  = ["BTC", "BBR", "BCN", "BELA", "BITS", "BLK", "BTCD", "BTM", "BTS", "BURST", "C2", "CLAM", "CURE"]
        self.currencies += ["DASH", "DGB", "DOGE", "EMC2", "FLDC", "FLO", "GAME", "GRC", "HUC", "HZ", "LTC"]
        self.currencies += ["OMNI", "MYR", "NAUT", "NAV", "NEOS", "NMC", "NOBL", "NOTE", "NSR", "NXT", "PINK", "POT"]
        self.currencies += ["PPC", "QBK", "QTL", "RBY", "RIC", "SDC", "SJCX", "SYS", "UNITY", "VIA"]
        self.currencies += ["XVC", "VRC", "VTC", "XBC", "XCP", "XEM", "XMG", "XMR", "XPM", "XRP"]
        self.currencies += ["USDT", "STR", "XMR", "XRP", "BCN", "MAID"]
        self.currencies += ["QORA", "IOC", "ETH", "SC", "BCY", "EXP", "FCT", "RADS", "AMP", "VOX", "DCR"]
        self.currencies += ["LSK", "LBC", "STEEM", "SBD", "ETC", "REP"]
        self.currencies += ["ARDR", "ZEC", "STRAT", "NXC"]

        self.currency = "BTC"
        sleep()

    def testSchema(self):
        r = ccs.poloniex.public.returnLoanOrders(self.currency)
        jsonschema.validate(json.loads(r), schema())

    @unittest.skip("time-consuming")
    def testCurrencies(self):
        for currency in self.currencies:
            r = ccs.poloniex.public.returnTradeHistory(currency)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.currency = "abcd"

    def testPair(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.poloniex.public.returnTradeHistory(self.currency)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
