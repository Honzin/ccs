import unittest
import ccs
import jsonschema
import json
import time

class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btcusd", "ltcusd", "ltcbtc", "ethusd", "ethbtc", "etcbtc", "etcusd", "bfxusd", "bfxbtc", "rrtusd", "rrtbtc", "zecusd", "zecbtc", "xmrusd", "xmrbtc"]
        self.schema = ccs.bitfinex.configuration.SCHEMA["ticker"]

    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.bitfinex.public.ticker(symbol)
            jsonschema.validate(json.loads(r), self.schema)
            time.sleep(3)

class Invalid(unittest.TestCase):
    def setUp(self):
        self.fail_symbol = "abcdef"
        self.schema = ccs.bitfinex.configuration.SCHEMA["ticker"]

    def testSymbol(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bitfinex.public.ticker(self.fail_symbol)
            jsonschema.validate(json.loads(r), self.schema)


if __name__ == '__main__':
    unittest.main()
