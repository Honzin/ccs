# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Bitstamp. This endpoint offer informations about conversion rate between EUR and USD.
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
    return ccs.bitstamp.configuration.SCHEMA["eurUsdConversionRate"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        sleep()

    def testSchema(self):
        r = ccs.bitstamp.public.eurUsdConversionRate()
        jsonschema.validate(json.loads(r), schema())


class Invalid(unittest.TestCase):
    def setUp(self):
        self.symbol = "aaabbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = '{"error": "Invalid request"}'
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
