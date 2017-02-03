import unittest
import ccs
import jsonschema
import json
import time

class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btcusd", "ltcusd", "ltcbtc", "ethusd", "ethbtc", "etcbtc", "etcusd", "bfxusd", "bfxbtc", "rrtusd", "rrtbtc", "zecusd", "zecbtc", "xmrusd", "xmrbtc"]
        self.schema = ccs.bitfinex.configuration.SCHEMA["orderbook"]
        time.sleep(7)

    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.bitfinex.public.orderbook(symbol)
            jsonschema.validate(json.loads(r), self.schema)
            time.sleep(3)

    def testLimitAsks(self):
        symbol = self.symbols[0]
        la = 10
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    def testLimitAsksFloat(self):
        symbol = self.symbols[0]
        la = 10.0
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    def testLimitAsksFloat1(self):
        symbol = self.symbols[0]
        la = 10.1
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), la)

    def testLimitAsksString(self):
        symbol = self.symbols[0]
        la = "10"
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["asks"]), int(la))


    def testLimitBids(self):
        symbol = self.symbols[0]
        lb = 10
        r = ccs.bitfinex.public.orderbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)


    def testLimitBidsFloat(self):
        symbol = self.symbols[0]
        lb = 10.0
        r = ccs.bitfinex.public.orderbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)


    def testLimitBidsFloat1(self):
        symbol = self.symbols[0]
        lb = 10.1
        r = ccs.bitfinex.public.orderbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), lb)


    def testLimitBidsString(self):
        symbol = self.symbols[0]
        lb = "10"
        r = ccs.bitfinex.public.orderbook(symbol, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), int(lb))

    def testLimitAsksBids(self):
        symbol = self.symbols[0]
        la = 10
        lb = 10
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la, limit_bids=lb)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), int(lb))
        self.assertLessEqual(len(d["asks"]), int(la))

    def testGroup0(self):
        symbol = self.symbols[0]
        g = 0
        r = ccs.bitfinex.public.orderbook(symbol, group=g)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

    def testGroup1(self):
        symbol = self.symbols[0]
        g = 1
        r = ccs.bitfinex.public.orderbook(symbol, group=g)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

    def testGroupFloat(self):
        symbol = self.symbols[0]
        g = 1.0
        r = ccs.bitfinex.public.orderbook(symbol, group=g)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

    def testGroupString(self):
        symbol = self.symbols[0]
        g = "1"
        r = ccs.bitfinex.public.orderbook(symbol, group=g)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

    def testLimitAsksBidsGroup(self):
        symbol = self.symbols[0]
        la = 10
        lb = 10
        g = 0
        r = ccs.bitfinex.public.orderbook(symbol, limit_asks=la, limit_bids=lb, group=g)
        d = json.loads(r)
        jsonschema.validate(d, self.schema)

        self.assertLessEqual(len(d["bids"]), int(lb))
        self.assertLessEqual(len(d["asks"]), int(la))


class Invalid(unittest.TestCase):
    def setUp(self):
        self.fail_symbol = "abcdef"
        self.symbol = "btcusd"
        self.schema = ccs.bitfinex.configuration.SCHEMA["orderbook"]
        time.sleep(5)

    def testSymbol(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bitfinex.public.orderbook(self.fail_symbol)
            jsonschema.validate(json.loads(r), self.schema)

    # Here should be more tests for invalid values of paramteres but Bitfinex server is able handle it.
    # It is show in trades.py.



if __name__ == '__main__':
    unittest.main()
