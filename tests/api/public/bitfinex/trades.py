import unittest
import ccs
import jsonschema
import json
import time

class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btcusd", "ltcusd", "ltcbtc", "ethusd", "ethbtc", "etcbtc", "etcusd", "bfxusd", "bfxbtc", "rrtusd", "rrtbtc", "zecusd", "zecbtc", "xmrusd", "xmrbtc"]
        self.schema = ccs.bitfinex.configuration.SCHEMA["trades"]
        time.sleep(2)

    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.bitfinex.public.trades(symbol)
            jsonschema.validate(json.loads(r), self.schema)
            time.sleep(3)

    def testTimestamp(self):
        symbol = self.symbols[0]
        t = 1482485015
        r = ccs.bitfinex.public.trades(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], t)

    def testTimestampLimit(self):
        symbol = self.symbols[0]
        t = 1482485015
        l = 10
        r = ccs.bitfinex.public.trades(symbol, timestamp=t, limit_trades=l)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], t)
        self.assertLessEqual(len(d), l)


    def testTimestampLow(self):
        symbol = self.symbols[0]
        t = 100
        r = ccs.bitfinex.public.trades(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], t)

    def testTimestampFloat(self):
        symbol = self.symbols[0]
        t = 1482485015.1
        r = ccs.bitfinex.public.trades(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], t)

    def testTimestampString(self):
        symbol = self.symbols[0]
        t = "1482185015"
        r = ccs.bitfinex.public.trades(symbol, timestamp=t)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertGreaterEqual(d[0]["timestamp"], int(t))

    def testLimit(self):
        symbol = self.symbols[0]
        l = 10
        r = ccs.bitfinex.public.trades(symbol, limit_trades=l)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d), l)

    def testLimitFloat(self):
        symbol = self.symbols[0]
        l = 10.0
        r = ccs.bitfinex.public.trades(symbol, limit_trades=l)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d), l)

    def testLimitString(self):
        symbol = self.symbols[0]
        l = "10"
        r = ccs.bitfinex.public.trades(symbol, limit_trades=l)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d), int(l))



class Invalid(unittest.TestCase):
    def setUp(self):
        self.fail_symbol = "abcdef"
        self.symbol = "btcusd"
        self.schema = ccs.bitfinex.configuration.SCHEMA["trades"]
        time.sleep(5)

    def testSymbol(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bitfinex.public.trades(self.fail_symbol)
            jsonschema.validate(json.loads(r), self.schema)

    # # This tests dont pass becuase Bitfinex server handle this invalid values of parametres and response contains valid array of trades.
    #
    # def testTimestampNegative(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, timestamp=-100)
    #         jsonschema.validate(json.loads(r), self.schema)
    #
    # def testTimestampString(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, timestamp="abcd")
    #         jsonschema.validate(json.loads(r), self.schema)
    #
    # def testTimestampMix(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, timestamp="11abcd")
    #         jsonschema.validate(json.loads(r), self.schema)
    #
    # def testLimitNegative(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, limit_trades=-10)
    #         jsonschema.validate(json.loads(r), self.schema)
    #
    # def testLimitString(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, limit_trades="abcd")
    #         jsonschema.validate(json.loads(r), self.schema)
    #
    # def testLimitMix(self):
    #     with self.assertRaises(jsonschema.exceptions.ValidationError):
    #         r = ccs.bitfinex.public.trades(self.symbol, limit_trades="11aa")
    #         jsonschema.validate(json.loads(r), self.schema)




if __name__ == '__main__':
    unittest.main()
