import unittest
import ccs
import time

####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BITFINEX
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        self.orderbook = ccs.orderbook(self.stock, self.base, self.quote)
        self.ordersA = self.orderbook.asks()
        self.ordersB = self.orderbook.bids()
        self.m = ccs.bitfinex.public.response
        # time.sleep(3)

    def testLen(self):
        self.assertIsInstance(len(self.ordersA), int)
        self.assertIsInstance(len(self.ordersB), int)

    def testGetItem(self):
        self.assertIsInstance(self.ordersA[0], self.m.Order)
        self.assertIsInstance(self.ordersB[0], self.m.Order)

    def testStock(self):
        self.assertEqual(self.ordersA.stock(), self.stock)
        self.assertEqual(self.ordersB.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.ordersA.method(), ccs.constants.ORDERS)
        self.assertEqual(self.ordersB.method(), ccs.constants.ORDERS)

    def testUsymbol(self):
        self.assertEqual(self.ordersA.usymbol(), self.base + ":" + self.quote)
        self.assertEqual(self.ordersB.usymbol(), self.base + ":" + self.quote)

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








