# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Btce. This endpoint offer informations about trades.
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


def schema():
    return ccs.btce.configuration.SCHEMA["trades"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self.pairs = ["btc_usd", "btc_rur", "btc_eur", "ltc_btc", "ltc_usd", "ltc_rur", "ltc_eur", "nmc_btc", "nmc_usd", "nvc_btc", "nvc_usd",
                      "usd_rur", "eur_usd", "eur_rur", "ppc_btc", "ppc_usd", "dsh_btc", "dsh_usd", "eth_btc", "eth_usd", "eth_eur", "eth_ltc", "eth_rur"]
        self.pair  = self.pairs[0]
        sleep()

    def testSchema(self):
        r = ccs.btce.public.trades(self.pair)
        jsonschema.validate(json.loads(r), schema())

    def testLimit(self):
        l = 2
        r = ccs.btce.public.trades(self.pair, limit=2)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        self.assertLessEqual(len(d[self.pair]), l)

    @unittest.skip("time-consuming")
    def testSymbols(self):
        for pair in self.pairs:
            r = ccs.btce.public.trades(pair)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.pair = "aaa_bbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.btce.public.trades(self.pair)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
