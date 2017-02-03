import unittest
import ccs
import jsonschema
import json
import time

class Valid(unittest.TestCase):
    def setUp(self):
        self.currencies = ["btc", "usd", "ltc", "ltc", "eth", "etc", "bfx", "zec", "zec"]
        self.schema = ccs.bitfinex.configuration.SCHEMA["lends"]
        time.sleep(3)

    def testCurrencies(self):
        # rrt and xmr fail probably doesnt exist fundingbook for this currency
        for currency in self.currencies:
            r = ccs.bitfinex.public.lends(currency)
            jsonschema.validate(json.loads(r), self.schema)
            time.sleep(3)

    def testLimitAsks(self):
        symbol = self.currencies[0]
        ll = 10
        r = ccs.bitfinex.public.lends(symbol, limit_lends=ll)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d[0]), ll)

    def testLimitAsksFloat(self):
        symbol = self.currencies[0]
        ll = 10.0
        r = ccs.bitfinex.public.lends(symbol, limit_lends=ll)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d[0]), ll)

    def testLimitAsksFloat1(self):
        symbol = self.currencies[0]
        ll = 10.1
        r = ccs.bitfinex.public.lends(symbol, limit_lends=ll)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d[0]), ll)

    def testLimitAsksString(self):
        symbol = self.currencies[0]
        ll = "10"
        r = ccs.bitfinex.public.lends(symbol, limit_lends=ll)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d[0]), int(ll))


    def testTimestamp(self):
        symbol = self.currencies[0]
        t = 1482085015
        r = ccs.bitfinex.public.lends(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], t)

    def testTimestampFloat(self):
        symbol = self.currencies[0]
        t = 1482085015.1
        r = ccs.bitfinex.public.lends(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], float(t))

    def testTimestampString(self):
        symbol = self.currencies[0]
        t = "1482085015"
        r = ccs.bitfinex.public.lends(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], float(t))


class Invalid(unittest.TestCase):
    def setUp(self):
        self.fail_currency = "abc"
        self.symbol = "btc"
        self.schema = ccs.bitfinex.configuration.SCHEMA["lends"]
        time.sleep(5)

    def testCurrency(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bitfinex.public.lends(self.fail_currency)
            jsonschema.validate(json.loads(r), self.schema)

    # Here should be more tests for invalid values of paramteres but Bitfinex server is able handle it.
    # It is show in trades.py.



if __name__ == '__main__':
    unittest.main()
