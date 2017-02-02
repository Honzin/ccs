import unittest
import ccs
import time

####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCC
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.CNY
        self.trades = ccs.trades(self.stock, self.base, self.quote)
        self.m = ccs.btcc.public.response
        #time.sleep(3)

    def testLen(self):
        self.assertIsInstance(len(self.trades), int)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], self.m.Trade)

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








