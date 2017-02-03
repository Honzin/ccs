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

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.btccusd.public.response.Trade)

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