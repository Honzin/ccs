import unittest
import ccs
import datetime
import time

####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BITFINEX
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        self.trades = ccs.trades(self.stock, self.base, self.quote)
        self.trade = self.trades[0]
        self.types = [ccs.constants.BUY, ccs.constants.SELL, ccs.constants.UNDEFINED]
        #time.sleep(3)


    def testTid(self):
        self.assertIsInstance(self.trade.tid(), float)

    def testPrice(self):
        self.assertIsInstance(self.trade.price(), float)

    def testAmount(self):
        self.assertIsInstance(self.trade.amount(), float)

    def testType(self):
        self.assertIn(self.trade.type(), self.types)

    def testTimestamp(self):
        self.assertIsInstance(self.trade.timestamp(), float)

    def testDt(self):
        self.assertIsInstance(self.trade.dt(), datetime.datetime)

    def testStock(self):
        self.assertEqual(self.trades.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.trades.method(), ccs.constants.TRADES)

    def testUsymbol(self):
        self.assertEqual(self.trades.usymbol(), self.base + ":" + self.quote)

    def testOsymbol(self):
        pass

    def testData(self):
        pass

    def testRaw(self):
        pass

    def testStr(self):
        pass


if __name__ == '__main__':
    unittest.main()








