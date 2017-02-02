import unittest
import ccs
import datetime

####################################################################################################################
# BTCCPRO                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"ticker":{"BidPrice":6003,"AskPrice":6017,"Open":6061.859999999999,"High":6083.4,"Low":5877,"Last":6005,"LastQuantity":5,"PrevCls":5974,"Volume":3834,"Volume24H":16495,"Timestamp":1484822829240,"ExecutionLimitDown":5881.1,"ExecutionLimitUp":6246.8}}'
        symbol = ccs.btccpro.Symbol(ccs.constants.XBT, ccs.constants.CNY)
        self.ticker = ccs.btccpro.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 5877)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 6083.4)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 6017)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 6003)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 6005)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 16495)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1484822829240)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2017, 1, 19, 10, 50, 59, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((6017 - 6003) / 6017) * 100)