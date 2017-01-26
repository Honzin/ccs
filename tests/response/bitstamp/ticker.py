import unittest
import ccs
import datetime


####################################################################################################################
# BITSTAMP                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"high": "765.00", "last": "759.01", "timestamp": "1480859680", "bid": "758.99", "vwap": "759.67", "volume": "2858.43054110", "low": "752.41", "ask": "759.00", "open": 762.97}'
        symbol = ccs.bitstamp.Symbol(ccs.constants.BTC, ccs.constants.USD)
        self.ticker = ccs.bitstamp.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 752.41)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 765.00)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 759.00)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 758.99)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 759.01)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 2858.43054110)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1480859680)

    def testDt(self):

        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 54, 40, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((759.00 - 758.99) / 759.00) * 100)