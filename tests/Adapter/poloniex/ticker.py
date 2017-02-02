import unittest
import ccs
import datetime
import time

####################################################################################################################
# POLONIEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.POLONIEX
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.LTC
        self.ticker = ccs.ticker(self.stock, self.base, self.quote)
        #time.sleep(3)

    def testLow(self):
        self.assertIsInstance(self.ticker.low(), float)

    def testHigh(self):
        self.assertIsInstance(self.ticker.high(), float)

    def testAsk(self):
        self.assertIsInstance(self.ticker.ask(), float)

    def testBid(self):
        self.assertIsInstance(self.ticker.bid(), float)

    def testLast(self):
        self.assertIsInstance(self.ticker.last(), float)

    def testVolume24h(self):
        self.assertIsInstance(self.ticker.volume24h(), float)

    def testTimestamp(self):
        self.assertIsInstance(self.ticker.timestamp(), float)

    def testDt(self):
        self.assertIsInstance(self.ticker.dt(), datetime.datetime)

    def testSpread(self):
        self.assertIsInstance(self.ticker.spread(), float)

    def testStock(self):
        self.assertEqual(self.ticker.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.ticker.method(), ccs.constants.TICKER)

    def testUsymbol(self):
        self.assertEqual(self.ticker.usymbol(), self.base + ":" + self.quote)

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








