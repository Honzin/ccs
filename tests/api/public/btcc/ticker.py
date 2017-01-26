# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Btcc-spot. This endpoint offer tick informations.
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
    return ccs.btcc.configuration.SCHEMA["ticker"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self. markets = ['btccny', "ltccny"]
        self.market = self.markets[0]
        sleep()

    def testSchema(self):
        r = ccs.btcc.public.ticker(self.market)
        jsonschema.validate(json.loads(r), schema())

    @unittest.skip("time-consuming")
    def testCurrencies(self):
        for market in self.markets:
            r = ccs.btcc.public.ticker(market)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.market = "aaabbb"

    # TODO Solve test & catch JSONDecodeError
    @unittest.skip("JSON='' -> JSONDecodeError")
    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.btcc.public.trades(self.market)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
