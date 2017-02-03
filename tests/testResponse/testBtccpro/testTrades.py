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
        self.trades = ccs.btccpro.public.response.Trades(self.json)
        self.m = ccs.btccpro.public.response

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], self.m.Trade)

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