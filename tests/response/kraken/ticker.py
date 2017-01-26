import unittest
import ccs
import datetime

####################################################################################################################
# KRAKEN                                                                                                           #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"error":[],"result":{"XXBTZEUR":{"a":["728.35400","1","1.000"],"b":["726.80300","3","3.000"],"c":["726.48000","0.33312654"],"v":["1056.79042830","2158.92713857"],"p":["724.41783","723.40158"],"t":[1696,3315],"l":["719.28000","718.37700"],"h":["729.64900","729.64900"],"o":"722.17000"}}}'
        symbol = ccs.kraken.Symbol(ccs.constants.BTC, ccs.constants.EUR)
        self.ticker = ccs.kraken.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 718.37700)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 729.64900)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 728.35400)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 726.80300)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 726.48000)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 2158.92713857)

    # TIMESTAMP IS EMULATED
    def testTimestamp(self):
        pass
    #     self.assertEqual(self.ticker.timestamp(), 1480859797)

    def testDt(self):
        pass
    #     self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2016, 12, 4, 13, 56, 37, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((728.35400 - 726.80300) / 728.35400) * 100)