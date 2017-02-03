import unittest
import ccs
import datetime

####################################################################################################################
# BTER                                                                                                             #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"result":"true","last":6096.21,"high":6160,"low":5749.99,"avg":5991.3,"sell":6091.2,"buy":6088.6,"vol_btc":237.571,"vol_cny":1423360.1,"rate_change_percentage":"-0.87"}'
        symbol = ccs.bter.Symbol(ccs.constants.BTC, ccs.constants.CNY)
        self.ticker = ccs.bter.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 5749.99)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 6160)

    # TODO valid ASK = SELL
    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 6091.2)

    # TODO valid BID = BUY
    def testBid(self):
        self.assertEqual(self.ticker.bid(), 6088.6)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 6096.21)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 0)

    # @unittest.skip("timestamp is emulated")
    def testTimestamp(self):
        self.assertAlmostEqual(self.ticker.timestamp(), datetime.datetime.now().timestamp(), delta=50)

    # @unittest.skip("timestamp is emulated")
    def testDt(self):
        dt = self.ticker.dt(tz=self.tz)
        dtnow = datetime.datetime.now()

        # This test should be valid in the middle of day (not midnight)
        self.assertAlmostEqual(dt.year, dtnow.year, delta=1)
        self.assertAlmostEqual(dt.month, dtnow.month, delta=1)
        self.assertAlmostEqual(dt.day, dtnow.day, delta=1)

        # This test should be valid in the middle of hour (not midnight)
        self.assertAlmostEqual(dt.hour, dtnow.hour, delta=1)
        self.assertAlmostEqual(dt.minute, dtnow.minute, delta=1)

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((6091.2 - 6088.6) / 6091.2) * 100)