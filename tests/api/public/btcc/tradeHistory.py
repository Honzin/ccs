# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Btcc-spot. This endpoint offer informations about trades.
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
    return ccs.btcc.configuration.SCHEMA["tradeHistory"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self. markets = ['btccny', "ltccny"]
        self.market = self.markets[0]
        sleep()

    def testSchema(self):
        r = ccs.btcc.public.tradeHistory(self.market)
        jsonschema.validate(json.loads(r), schema())

    def testLimit(self):
        l = 2
        r = ccs.btcc.public.tradeHistory(self.market, limit=l)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        self.assertLessEqual(len(d), l)

    def testSinceId(self):
        s = 7000
        r = ccs.btcc.public.tradeHistory(self.market, since=s)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        for t in d:
            self.assertGreaterEqual(int(t["tid"]), s)

    def testSinceTime(self):
        s = 1484396000
        st = "time"
        r = ccs.btcc.public.tradeHistory(self.market, since=s, sincetype=st)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        for t in d:
            self.assertGreaterEqual(int(t["date"]), s)

    @unittest.skip("time-consuming")
    def testCurrencies(self):
        for market in self.markets:
            r = ccs.btcc.public.tradeHistory(market)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.market = "aaabbb"

    # TODO Solve test & catch JSONDecodeError
    @unittest.skip("JSON='' -> JSONDecodeError")
    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.btcc.public.tradeHistory(self.market)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
