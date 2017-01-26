import unittest
import ccs
import datetime
import json


####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"mid":"767.415","bid":"767.41","ask":"767.42","last_price":"767.49","low":"760.0","high":"768.96","volume":"2685.95891399","timestamp":"1480858375.486312041"}'
        self.cur1 = ccs.constants.BTC
        self.cur2 = ccs.constants.USD
        symbol = ccs.bitfinex.Symbol(self.cur1, self.cur2)
        self.ticker = ccs.bitfinex.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 760.0)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 768.96)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 767.42)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 767.41)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 767.49)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 2685.95891399)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1480858375.486312041)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 32, 55, 486312, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((767.42 - 767.41) / 767.42) * 100)

    ####################################################################################################################
    # Advanced tests (Bitfinex test case will test it for all)                                                         #
    ####################################################################################################################

    def testOsymbol(self):
        self.assertEqual(self.ticker.osymbol(), self.cur1.lower() + self.cur2.lower())

    def testUsymbol(self):
        self.assertEqual(self.ticker.usymbol(), self.cur1.lower() + ":" + self.cur2.lower())

    def testMethod(self):
        self.assertEqual(self.ticker.method(), "ticker")

    def testStock(self):
        self.assertEqual(self.ticker.stock(), ccs.constants.BITFINEX)

    def testStr(self):
        d = json.loads(str(self.ticker))
        self.assertAlmostEqual(d[ccs.constants.LOW], 760.0)
        self.assertAlmostEqual(d[ccs.constants.HIGH], 768.96)
        self.assertAlmostEqual(d[ccs.constants.ASK], 767.42)
        self.assertAlmostEqual(d[ccs.constants.BID], 767.41)
        self.assertAlmostEqual(d[ccs.constants.LAST], 767.49)
        self.assertAlmostEqual(d[ccs.constants.VOLUME24H], 2685.95891399)
        self.assertAlmostEqual(d[ccs.constants.TIMESTAMP], 1480858375.486312041)
        self.assertAlmostEqual(d[ccs.constants.STOCK], ccs.constants.BITFINEX)



