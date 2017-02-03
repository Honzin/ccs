# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Bitfinex. This endpoint offer information about fundingbook.
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

class Valid(unittest.TestCase):
    def setUp(self):
        self.currencies = ["btc", "usd", "ltc", "ltc", "eth", "etc", "bfx", "zec", "zec"]
        self.schema = ccs.bitfinex.configuration.SCHEMA["fundingbook"]
        time.sleep(7)

    def testSchema(self):
        r = ccs.bitfinex.public.fundingbook("btc")
        jsonschema.validate(json.loads(r), self.schema)
        time.sleep(3)

    def testCurrencies(self):
        # rrt and xmr fail probably doesnt exist fundingbook for this currency
        for currency in self.currencies:
            r = ccs.bitfinex.public.fundingbook(currency)
            jsonschema.validate(json.loads(r), self.schema)
            time.sleep(3)

    def testLimitAsks(self):
        symbol = self.currencies[0]
        la = 10
        r = ccs.bitfinex.public.fundingbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    @unittest.skip("it is not necessary")
    def testLimitAsksFloat(self):
        symbol = self.currencies[0]
        la = 10.0
        r = ccs.bitfinex.public.fundingbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    @unittest.skip("it is not necessary")
    def testLimitAsksFloat1(self):
        symbol = self.currencies[0]
        la = 10.1
        r = ccs.bitfinex.public.fundingbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    @unittest.skip("it is not necessary")
    def testLimitAsksString(self):
        symbol = self.currencies[0]
        la = "10"
        r = ccs.bitfinex.public.fundingbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), int(la))


    def testLimitBids(self):
        symbol = self.currencies[0]
        lb = 10
        r = ccs.bitfinex.public.fundingbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)

    @unittest.skip("it is not necessary")
    def testLimitBidsFloat(self):
        symbol = self.currencies[0]
        lb = 10.0
        r = ccs.bitfinex.public.fundingbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)

    @unittest.skip("it is not necessary")
    def testLimitBidsFloat1(self):
        symbol = self.currencies[0]
        lb = 10.1
        r = ccs.bitfinex.public.fundingbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)

    @unittest.skip("it is not necessary")
    def testLimitBidsString(self):
        symbol = self.currencies[0]
        lb = "10"
        r = ccs.bitfinex.public.fundingbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), int(lb))

    def testLimitAsksBids(self):
        symbol = self.currencies[0]
        la = 10
        lb = 10
        r = ccs.bitfinex.public.fundingbook(symbol, limit_asks=la, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), int(lb))
        self.assertLessEqual(len(d["asks"]), int(la))


class Invalid(unittest.TestCase):
    def setUp(self):
        self.fail_currency = "abc"
        self.symbol = "btc"
        self.schema = ccs.bitfinex.configuration.SCHEMA["fundingbook"]
        time.sleep(5)

    def testCurrency(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bitfinex.public.fundingbook(self.fail_currency)
            jsonschema.validate(json.loads(r), self.schema)

    # Here should be more tests for invalid values of paramteres but Bitfinex server is able handle it.



if __name__ == '__main__':
    unittest.main()
