import unittest
import ccs
import datetime


####################################################################################################################
# BITFINEX                                                                                                         #
####################################################################################################################

class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"mid":"767.415","bid":"767.41","ask":"767.42","last_price":"767.49","low":"760.0","high":"768.96","volume":"2685.95891399","timestamp":"1480858375.486312041"}'
        self.currency = ccs.constants.BTC + ccs.constants.USD
        self.ticker = ccs.bitfinex.public.response.Ticker(self.json, self.currency)

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
# BITSTAMP                                                                                                         #
####################################################################################################################

class Bitstamp(Bitfinex):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"high": "765.00", "last": "759.01", "timestamp": "1480859680", "bid": "758.99", "vwap": "759.67", "volume": "2858.43054110", "low": "752.41", "ask": "759.00", "open": 762.97}'
        self.currency = ccs.constants.BTC + ccs.constants.USD
        self.ticker = ccs.bitstamp.public.response.Ticker(self.json, self.currency)

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



####################################################################################################################
# BTCC                                                                                                             #
####################################################################################################################

class Btcc(Bitfinex):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"ticker": {"high": "5430.00", "low": "5350.00", "buy": "5425.77", "sell": "5425.87", "last": "5425.98","vol": "1165699.19230000", "date": 1480859730, "vwap": "5402.76", "prev_close": "5391.56", "open": "5391.6"}}'
        self.currency = ccs.constants.BTC + ccs.constants.CNY
        self.ticker = ccs.btcc.public.response.Ticker(self.json, self.currency)

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

####################################################################################################################
# BTCE                                                                                                             #
####################################################################################################################

class Btce(Bitfinex):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"btc_usd":{"high":765,"low":750,"avg":757.5,"vol":1935696.62913,"vol_cur":2551.40496,"last":764.999,"buy":765.27,"sell":765.1,"updated":1480859797}}'
        self.currency = ccs.constants.BTC + ccs.constants.USD
        self.ticker = ccs.btce.public.response.Ticker(self.json, self.currency)

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


####################################################################################################################
# KRAKEN                                                                                                           #
####################################################################################################################

class Kraken(Bitfinex):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"error":[],"result":{"XXBTZEUR":{"a":["728.35400","1","1.000"],"b":["726.80300","3","3.000"],"c":["726.48000","0.33312654"],"v":["1056.79042830","2158.92713857"],"p":["724.41783","723.40158"],"t":[1696,3315],"l":["719.28000","718.37700"],"h":["729.64900","729.64900"],"o":"722.17000"}}}'
        self.currency = ccs.constants.BTC + ccs.constants.EUR
        self.ticker = ccs.kraken.public.response.Ticker(self.json, self.currency)

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


####################################################################################################################
# OKCOIN                                                                                                           #
####################################################################################################################

class Okcoin(Bitfinex):
    def setUp(self):
        self.tz = datetime.timezone.utc
        self.json = '{"date":"1480859886","ticker":{"buy":"768.8","high":"769.0","last":"768.23","low":"761.0","sell":"768.92","vol":"1158.384"}}'
        self.currency = ccs.constants.BTC + ccs.constants.USD
        self.ticker = ccs.okcoin.public.response.Ticker(self.json, self.currency)

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

if __name__ == '__main__':
    unittest.main()



