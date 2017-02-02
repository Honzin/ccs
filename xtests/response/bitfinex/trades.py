import unittest
import ccs

class Valid(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '[{"timestamp":1480850761,"tid":24902281,"price":"765.0","amount":"0.27731462","exchange":"bitfinex","type":"buy"},{"timestamp":1480850759,"tid":24902279,"price":"764.99","amount":"0.01907827","exchange":"bitfinex","type":"sell"}]'
        self.trades = ccs.bitfinex.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.bitfinex.public.response.Trade)

    def testMethod(self):
        pass

    def testStock(self):
        pass

    def testOsymbol(self):
        pass

    def testUsymbol(self):
        pass

    def testStr(self):
        pass