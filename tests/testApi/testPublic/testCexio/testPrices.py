# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Cexio. This endpoint offer informations about last price for given markets.
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
    return ccs.cexio.configuration.SCHEMA["lastPricesForGivenMarket"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self.currencies1 = ["BTC", "BTC", "BTC", "GHS", "LTC", "LTC", "BTC", "ETH", "ETH", "ETH"]
        self.currencies2 = ["USD", "EUR", "GBP", "BTC", "USD", "BTC", "RUB", "BTC", "USD", "EUR"]

        self.curr1 = self.currencies1[0]
        self.curr2 = self.currencies2[0]
        self.curr3 = self.currencies2[2]

        sleep()

    def testSchema(self):
        r = ccs.cexio.public.lastPricesForGivenMarket(self.curr1, self.curr2, self.curr3)
        jsonschema.validate(json.loads(r), schema())

    def testCurrencies(self):
        r = ccs.cexio.public.lastPricesForGivenMarket("BTC", "GHS", "LTC", "ETH", "EUR", "USD", "GBP", "RUB")
        jsonschema.validate(json.loads(r), schema())

class Invalid(unittest.TestCase):
    def setUp(self):
        self.curr1 = "aaa"
        self.curr2 = "bbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.cexio.public.lastPrice(self.curr1, self.curr2)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
