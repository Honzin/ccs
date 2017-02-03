import unittest
import ccs
import time

####################################################################################################################
# BTCCUSD                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCUSD
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD

        self.json = '{"asks":[[1038.97,0.188],[1049,0.5]],"bids":[[981.09,0.0004],[981.08,0.004]],"date":1486140539483}'
        symbol = ccs.btccusd.Symbol(self.base, self.quote)
        self.orderbook = ccs.btccusd.public.response.OrderBook(self.json, symbol)

        self.ordersA = self.orderbook.asks()
        self.ordersB = self.orderbook.bids()
        self.m = ccs.btccusd.public.response
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








