import unittest
import ccs
import datetime
import time

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
