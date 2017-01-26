import unittest
import ccs
import datetime

####################################################################################################################
# OKCOINCOM                                                                                                        #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"date":"1480859886","ticker":{"buy":"768.8","high":"769.0","last":"768.23","low":"761.0","sell":"768.92","vol":"1158.384"}}'
        symbol = ccs.okcoincom.Symbol(ccs.constants.BTC, ccs.constants.USD)
        self.ticker = ccs.okcoincom.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 761.0)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 769.0)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 768.8)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 768.92)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 768.23)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 1158.384)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1480859886)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 58, 6, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((768.8 - 768.92) / 768.8) * 100)