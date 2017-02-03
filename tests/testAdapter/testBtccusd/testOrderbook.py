import unittest
import ccs
import datetime
import time

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCUSD
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        self.orderbook = ccs.orderbook(self.stock, self.base, self.quote)
        self.m = ccs.btccusd.public.response
        #time.sleep(3)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), self.m.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), self.m.Orders)

    def testStock(self):
        self.assertEqual(self.orderbook.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.orderbook.method(), ccs.constants.ORDERBOOK)

    def testUsymbol(self):
        self.assertEqual(self.orderbook.usymbol(), self.base + ":" + self.quote)

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








