import unittest
import ccs
import time

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCPRO
        self.base = ccs.constants.XBT
        self.quote = ccs.constants.CNY
        symbol = ccs.btccpro.Symbol(self.base, self.quote)

        self.json = '{"asks":[[6929,22],[6930,25]],"bids":[[6910.3,11],[6903,4]],"date":1486145574689}'
        self.orderbook = ccs.btccpro.public.response.OrderBook(self.json, symbol)

        self.ordersA = self.orderbook.asks()
        self.ordersB = self.orderbook.bids()
        self.m = ccs.btccpro.public.response
        # time.sleep(3)

    def testLen(self):
        self.assertEqual(len(self.ordersA), 2)
        self.assertEqual(len(self.ordersB), 2)

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








