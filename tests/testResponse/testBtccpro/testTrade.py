import unittest
import ccs

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCPRO
        self.base = ccs.constants.XBT
        self.quote = ccs.constants.CNY
        symbol = ccs.btccpro.Symbol(self.base, self.quote)

        self.limit = 2

        self.json = '[{"Id":3,"Timestamp":1445592744686,"Price":1778,"Quantity":1,"Side":"Buy"},{"Id":4,"Timestamp":1445594157046,"Price":1780,"Quantity":1,"Side":"Sell"}]'
        self.trades = ccs.btccpro.public.response.Trades(self.json, symbol)
        self.trade1 = self.trades[0]

        self.data = {"Id":3,"Timestamp":1445592744686,"Price":1778,"Quantity":1,"Side":"Buy"}
        self.trade2 = ccs.btccpro.public.response.Trade(self.data, symbol)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 3)
        self.assertEqual(self.trade2.tid(), 3)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 1778)
        self.assertEqual(self.trade2.price(), 1778)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 1)
        self.assertEqual(self.trade2.amount(), 1)

    def testType(self):
        self.assertEqual(self.trade1.type(), "buy")
        self.assertEqual(self.trade2.type(), "buy")
        self.assertEqual(self.trade3.type(), "sell")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1445592744686)
        self.assertEqual(self.trade2.timestamp(), 1445592744686)

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

