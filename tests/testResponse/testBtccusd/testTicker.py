import unittest
import ccs
import datetime

####################################################################################################################
# BTCCUSD                                                                                                          #
####################################################################################################################

class Valid(unittest.TestCase):
    def setUp(self):
        self.stock = ccs.constants.BTCCUSD
        self.base = ccs.constants.BTC
        self.quote = ccs.constants.USD
        symbol = ccs.btccusd.Symbol(self.base, self.quote)

        self.tz = datetime.timezone.utc
        self.json = '{"ticker":{"BidPrice":980.01,"AskPrice":1028.99,"Open":989.52,"High":1045,"Low":940,"Last":1028.99,"LastQuantity":0.0467,"PrevCls":971.01,"Volume":6.9446,"Volume24H":7.1426,"Timestamp":1486043433389,"ExecutionLimitDown":848.09,"ExecutionLimitUp":1147.41}}'
        self.ticker = ccs.btccusd.public.response.Ticker(self.json, symbol)

    def testLow(self):
        self.assertEqual(self.ticker.low(), 940)

    def testHigh(self):
        self.assertEqual(self.ticker.high(), 1045)

    def testAsk(self):
        self.assertEqual(self.ticker.ask(), 1028.99)

    def testBid(self):
        self.assertEqual(self.ticker.bid(), 980.01)

    def testLast(self):
        self.assertEqual(self.ticker.last(), 1028.99)

    def testVolume24h(self):
        self.assertEqual(self.ticker.volume24h(), 7.1426)

    def testTimestamp(self):
        self.assertEqual(self.ticker.timestamp(), 1486043433)

    def testDt(self):
        self.assertEqual(self.ticker.dt(tz=self.tz), datetime.datetime(2017, 2, 2, 13, 50, 33, tzinfo=self.tz))

    def testSpread(self):
        self.assertEqual(self.ticker.spread(), ((1028.99 - 980.01) / 1028.99) * 100)