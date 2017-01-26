import unittest
import ccs
import datetime

####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"mid":"767.415","bid":"767.41","ask":"767.42","last_price":"767.49","low":"760.0","high":"768.96","volume":"2685.95891399","timestamp":"1480858375.486312041"}'
        self.currency = ccs.constants.BTC + ccs.constants.USD
        self.ticker = ccs.bitfinex.public.response.Ticker(self.json, self.currency)



    def testLow(self):
        pass