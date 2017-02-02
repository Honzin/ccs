import unittest
import ccs
import time

####################################################################################################################
# BTCE                                                                                                             #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCE
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        self.orderbook = ccs.orderbook(self.stock, self.base, self.quote)
        self.ordersA = self.orderbook.asks()
        self.orderA = self.ordersA[0]
        self.ordersB = self.orderbook.bids()
        self.orderB = self.ordersB[0]
        self.m = ccs.btce.public.response
        # time.sleep(3)

    def testPrice(self):
        self.assertIsInstance(self.orderA.price(), float)
        self.assertIsInstance(self.orderB.price(), float)

    def testAmount(self):
        self.assertIsInstance(self.orderA.amount(), float)
        self.assertIsInstance(self.orderB.amount(), float)

    def testStock(self):
        self.assertEqual(self.orderA.stock(), self.stock)
        self.assertEqual(self.orderB.stock(), self.stock)

    def testMethod(self):
        self.assertEqual(self.orderA.method(), ccs.constants.ORDER)
        self.assertEqual(self.orderB.method(), ccs.constants.ORDER)

    def testUsymbol(self):
        self.assertEqual(self.orderA.usymbol(), self.base + ":" + self.quote)
        self.assertEqual(self.orderB.usymbol(), self.base + ":" + self.quote)

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








