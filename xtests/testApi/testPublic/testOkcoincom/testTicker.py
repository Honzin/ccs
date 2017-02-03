# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Okcoin.com. This endpoint offer tick informations.
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
    return ccs.okcoincom.configuration.SCHEMA["ticker"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btc_usd", "ltc_usd"]
        self.symbol = self.symbols[0]
        sleep()

    def testSchema(self):
        r = ccs.okcoincom.public.ticker(self.symbol)
        jsonschema.validate(json.loads(r), schema())

    @unittest.skip("time-consuming")
    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.okcoincom.public.ticker(symbol)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.symbol = "aaa_bbb"

    @unittest.skip("server is able recover")
    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.okcoincom.public.ticker(self.symbol)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
