import unittest
import ccs
import datetime

####################################################################################################################
# BTCE                                                                                                             #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"btc_usd":{"high":765,"low":750,"avg":757.5,"vol":1935696.62913,"vol_cur":2551.40496,"last":764.999,"buy":765.27,"sell":765.1,"updated":1480859797}}'
        symbol = ccs.btce.Symbol(ccs.constants.BTC, ccs.constants.USD)
        self.ticker = ccs.btce.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 750)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 765)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 765.27)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 765.1)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 764.999)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 1935696.62913)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1480859797)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 56, 37, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((765.27 - 765.1) / 765.27) * 100)