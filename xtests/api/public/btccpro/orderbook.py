# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Btcc-spot. This endpoint offer informations about orderbook.
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
    return ccs.btccpro.configuration.SCHEMA["orderbook"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self. markets = ['xbtcny']
        self.market = self.markets[0]
        sleep()

    def testSchema(self):
        r = ccs.btccpro.public.orderbook(self.market)
        jsonschema.validate(json.loads(r), schema())

    def testLimit(self):
        l = 2
        r = ccs.btccpro.public.orderbook(self.market, limit=l)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        self.assertLessEqual(len(d["asks"]), l)
        self.assertLessEqual(len(d["bids"]), l)


class Invalid(unittest.TestCase):
    def setUp(self):
        self.market = "aaabbb"

    # TODO Solve test & catch JSONDecodeError
    @unittest.skip("JSON='' -> JSONDecodeError")
    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.btccpro.public.orderbook(self.market)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
