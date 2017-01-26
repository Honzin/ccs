import unittest
import ccs
import datetime

####################################################################################################################
# CEXIO                                                                                                            #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"timestamp":"1484832214","low":"853","high":"908.218","last":"898.85","volume":"529.78497768","volume30d":"19771.36729506","bid":895.5261,"ask":898.85}'
        symbol = ccs.cexio.Symbol(ccs.constants.BTC, ccs.constants.USD)
        self.ticker = ccs.cexio.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 853)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 908.218)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 898.85)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 895.5261)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 898.85)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 529.78497768)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1484832214)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2017, 1, 19, 13, 23, 34, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((898.85 - 895.5261) / 898.85) * 100)