import unittest
import ccs

class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '[{"timestamp":1480850761,"tid":24902281,"price":"765.0","amount":"0.27731462","exchange":"bitfinex","type":"buy"},{"timestamp":1480850759,"tid":24902279,"price":"764.99","amount":"0.01907827","exchange":"bitfinex","type":"sell"}]'
        self.trades = ccs.bitfinex.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.bitfinex.public.response.Trade)



class Bitstamp(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '[{"date": "1480928480", "tid": 12584559, "price": "749.26", "type": 1, "amount": "0.00665990"}, {"date": "1480928462", "tid": 12584558, "price": "749.18", "type": 0, "amount": "0.45830000"}]'
        self.trades = ccs.bitstamp.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.bitstamp.public.response.Trade)


class Btcc(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '[{"date":"1480926246","price":5336.46,"amount":0.15,"tid":"104899229"},{"date":"1480926247","price":5336.53,"amount":11,"tid":"104899230"}]'
        self.trades = ccs.btcc.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.btcc.public.response.Trade)



class Btce(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '{"btc_usd":[{"type":"ask","price":753,"amount":0.133,"tid":88349995,"timestamp":1480931524},{"type":"bid","price":753,"amount":0.101,"tid":88349992,"timestamp":1480931522}]}'
        self.trades = ccs.btce.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.btce.public.response.Trade)


class Kraken(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '{"error":[],"result":{"XXBTZEUR":[["718.17700","0.26930000",1480922709.6833,"b","l",""],["718.33200","0.63766159",1480922720.8598,"s","l",""]],"last":"1480931987320941919"}}'
        self.trades = ccs.kraken.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.kraken.public.response.Trade)



class Okcoin(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = '[{"amount":"0.123","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781524,"type":"sell"},{"amount":"0.121","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781526,"type":"buy"}]'
        self.trades = ccs.okcoin.public.response.Trades(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.trades), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.trades[0], ccs.okcoin.public.response.Trade)


if __name__ == '__main__':
    unittest.main()