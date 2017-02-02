import unittest
import ccs
import datetime

####################################################################################################################
# BITTREX                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"success":true,"message":"","result":[{"MarketName":"BTC-LTC","High":0.00448995,"Low":0.00429397,"Volume":5351.00095158,"Last":0.00433176,"BaseVolume":23.37288450,"TimeStamp":"2017-01-19T10:14:24.12","Bid":0.00429704,"Ask":0.00433170,"OpenBuyOrders":164,"OpenSellOrders":823,"PrevDay":0.00434952,"Created":"2014-02-13T00:00:00"}]}'
        symbol = ccs.bittrex.Symbol(ccs.constants.BTC, ccs.constants.LTC)
        self.ticker = ccs.bittrex.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 0.00429397)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 0.00448995)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 0.00433170)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 0.00429704)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 0.00433176)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 5351.00095158)

    # TODO consider cut the float part
    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1484820864.12)

    # TODO consider cut the float part
    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2017, 1, 19, 10, 14, 24, 120000, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((0.00433170 - 0.00429704) / 0.00433170) * 100)
