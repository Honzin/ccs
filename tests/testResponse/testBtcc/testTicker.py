import unittest
import ccs
import datetime

####################################################################################################################
# BTCC                                                                                                             #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"ticker": {"high": "5430.00", "low": "5350.00", "buy": "5425.77", "sell": "5425.87", "last": "5425.98","vol": "1165699.19230000", "date": 1480859730, "vwap": "5402.76", "prev_close": "5391.56", "open": "5391.6"}}'
        symbol = ccs.btcc.Symbol(ccs.constants.BTC, ccs.constants.CNY)
        self.ticker = ccs.btcc.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 5350.00)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 5430.00)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 5425.77)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 5425.87)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 5425.98)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 1165699.19230000)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1480859730)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 55, 30, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((5425.77 - 5425.87) / 5425.77) * 100)