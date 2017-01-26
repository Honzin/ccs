import unittest
import ccs

####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '[{"timestamp":1480850761,"tid":24902281,"price":"765.0","amount":"0.27731462","exchange":"bitfinex","type":"buy"},{"timestamp":1480850759,"tid":24902279,"price":"764.99","amount":"0.01907827","exchange":"bitfinex","type":"sell"}]'
        self.trades = ccs.bitfinex.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"timestamp":1480850761, "tid":24902281, "price":"765.0", "amount":"0.27731462", "exchange":"bitfinex", "type":"buy"}
        self.trade2 = ccs.bitfinex.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 24902281)
        self.assertEqual(self.trade2.tid(), 24902281)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 765.0)
        self.assertEqual(self.trade2.price(), 765.0)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.27731462)
        self.assertEqual(self.trade2.amount(), 0.27731462)

    def testType(self):
        self.assertEqual(self.trade1.type(), "buy")
        self.assertEqual(self.trade2.type(), "buy")
        self.assertEqual(self.trade3.type(), "sell")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480850761)
        self.assertEqual(self.trade2.timestamp(), 1480850761)

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

