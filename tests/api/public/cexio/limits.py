# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Cexio. This endpoint offer informations about currencies.
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
    return ccs.cexio.configuration.SCHEMA["currencyLimits"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        pass

    def testSchema(self):
        r = ccs.cexio.public.currencyLimits()
        jsonschema.validate(json.loads(r), schema())


class Invalid(unittest.TestCase):
    def setUp(self):
        pass

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = '{"e":"Unspecified"}'
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
