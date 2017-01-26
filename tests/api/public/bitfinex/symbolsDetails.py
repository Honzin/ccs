import unittest
import ccs
import jsonschema
import json

class Valid(unittest.TestCase):
    def setUp(self):
        self.schema = ccs.bitfinex.configuration.SCHEMA["symbolsDetails"]

    def testSchema(self):
        r = ccs.bitfinex.public.symbolsDetails()
        jsonschema.validate(json.loads(r), self.schema)



class Invalid(unittest.TestCase):
    pass # Nothing for testing


if __name__ == '__main__':
    unittest.main()
