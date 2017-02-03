import unittest
import ccs

####################################################################################################################
# BTCCUSD                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCUSD
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        symbol = ccs.btccusd.Symbol(self.base, self.quote)

        self.limit = 2

        self.json = '[{"Id":7618,"Timestamp":1485830873401,"Price":969.96,"Quantity":0.092,"Side":"Buy"},{"Id":7619,"Timestamp":1485834001646,"Price":965,"Quantity":0.003,"Side":"Sell"}]'
        self.trades = ccs.btccusd.public.response.Trades(self.json, symbol)
        self.trade1 = self.trades[0]

        self.data = {"Id":7618,"Timestamp":1485830873401,"Price":969.96,"Quantity":0.092,"Side":"Buy"}
        self.trade2 = ccs.btccusd.public.response.Trade(self.data, symbol)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 7618)
        self.assertEqual(self.trade2.tid(), 7618)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 969.96)
        self.assertEqual(self.trade2.price(), 969.96)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.092)
        self.assertEqual(self.trade2.amount(), 0.092)

    def testType(self):
        self.assertEqual(self.trade1.type(), "buy")
        self.assertEqual(self.trade2.type(), "buy")
        self.assertEqual(self.trade3.type(), "sell")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1485830873401)
        self.assertEqual(self.trade2.timestamp(), 1485830873401)

    def testDt(self):
        pass

    def testMethod(self):
        pass

    def testStock(self):
        pass

    def testOsymbol(self):
        pass

    def testUsymbol(self):
        pass

    def testStr(self):
        pass


if __name__ == '__main__':
    unittest.main()

