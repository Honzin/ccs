import unittest
import ccs
import time
import datetime

####################################################################################################################
# BTCCUSD                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCUSD
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD

        self.tz = datetime.timezone.utc

        self.json = '{"asks":[[1038.97,0.188],[1049,0.5]],"bids":[[981.09,0.0004],[981.08,0.004]],"date":1486140539483}'
        symbol = ccs.btccusd.Symbol(self.base, self.quote)
        self.orderbook = ccs.btccusd.public.response.OrderBook(self.json, symbol)

        self.ordersA = self.orderbook.asks()
        self.orderA = self.ordersA[0]
        self.ordersB = self.orderbook.bids()
        self.orderB = self.ordersB[0]
        self.m = ccs.btccusd.public.response
        # time.sleep(3)

    def testPrice(self):
        self.assertEqual(self.orderA.price(), 1038.97)
        self.assertEqual(self.orderB.price(), 981.09)

    def testAmount(self):
        self.assertEqual(self.orderA.amount(), 0.188)
        self.assertEqual(self.orderB.amount(), 0.0004)

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








