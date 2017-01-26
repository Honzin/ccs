import unittest
import ccs
import jsonschema
import json

class Valid(unittest.TestCase):
    def setUp(self):
        self.schema = ccs.bitfinex.configuration.SCHEMA["symbols"]

    def testSchema(self):
        r = ccs.bitfinex.public.symbols()
        jsonschema.validate(json.loads(r), self.schema)


if __name__ == '__main__':
    unittest.main()
