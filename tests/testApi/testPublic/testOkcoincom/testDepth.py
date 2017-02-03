# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Okcoin.com. This endpoint offer informations about orderbook.
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
    return ccs.okcoincom.configuration.SCHEMA["depth"]


def sleep():
    time.sleep(3)

class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btc_usd", "ltc_usd"]
        self.symbol = self.symbols[0]
        sleep()

    def testSchema(self):
        r = ccs.okcoincom.public.depth(self.symbol)
        jsonschema.validate(json.loads(r), schema())

    def testSize(self):
        s = 2
        r = ccs.okcoincom.public.depth(self.symbol, size=s)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        self.assertLessEqual(len(d["asks"]), s)
        self.assertLessEqual(len(d["bids"]), s)


    def testMerge(self):
        # TODO nejsnosti v dokumentaci
        pass

    def testSizeMerge(self):
        # TODO nejsnosti v dokumentaci
        pass



    @unittest.skip("time-consuming")
    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.okcoincom.public.depth(symbol)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.symbol = "aaa_bbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.okcoincom.public.depth(self.symbol)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
