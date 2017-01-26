import unittest
import ccs

class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '[{"timestamp":1480850761,"tid":24902281,"price":"765.0","amount":"0.27731462","exchange":"bitfinex","type":"buy"},{"timestamp":1480850759,"tid":24902279,"price":"764.99","amount":"0.01907827","exchange":"bitfinex","type":"sell"}]'
        self.trades = ccs.bitfinex.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"timestamp":1480850761,"tid":24902281,"price":"765.0","amount":"0.27731462","exchange":"bitfinex","type":"buy"}
        self.trade2 = ccs.bitfinex.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 24902281)
        self.assertEqual(self.trade2.tid(), 24902281)


    def testPrice(self):
        self.assertEqual(self.trade1.price(), 765.0)
        self.assertEqual(self.trade2.price(), 765.0)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.27731462)
        self.assertEqual(self.trade2.amount(), 0.27731462)

    def testType(self):
        self.assertEqual(self.trade1.type(), "buy")
        self.assertEqual(self.trade2.type(), "buy")
        self.assertEqual(self.trade3.type(), "sell")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480850761)
        self.assertEqual(self.trade2.timestamp(), 1480850761)

# BITSTAMP
# [{"date": "1480928480", "tid": 12584559, "price": "749.26", "type": 1, "amount": "0.00665990"}, {"date": "1480928462", "tid": 12584558, "price": "749.18", "type": 0, "amount": "0.45830000"}]


class Bitstamp(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '[{"date": "1480928480", "tid": 12584559, "price": "749.26", "type": 1, "amount": "0.00665990"}, {"date": "1480928462", "tid": 12584558, "price": "749.18", "type": 0, "amount": "0.45830000"}]'
        self.trades = ccs.bitstamp.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"date": "1480928480", "tid": 12584559, "price": "749.26", "type": 1, "amount": "0.00665990"}
        self.trade2 = ccs.bitstamp.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 12584559)
        self.assertEqual(self.trade2.tid(), 12584559)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 749.26)
        self.assertEqual(self.trade2.price(), 749.26)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.00665990)
        self.assertEqual(self.trade2.amount(), 0.00665990)

    def testType(self):
        self.assertEqual(self.trade1.type(), "sell")
        self.assertEqual(self.trade2.type(), "sell")
        self.assertEqual(self.trade3.type(), "buy")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480928480)
        self.assertEqual(self.trade2.timestamp(), 1480928480)

# BTCC
# [{"date":"1480926246","price":5336.46,"amount":0.15,"tid":"104899229"},{"date":"1480926247","price":5336.53,"amount":11,"tid":"104899230"}]

class Btcc(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '[{"date":"1480926246","price":5336.46,"amount":0.15,"tid":"104899229"},{"date":"1480926247","price":5336.53,"amount":11,"tid":"104899230"}]'
        self.trades = ccs.btcc.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"date":"1480926246","price":5336.46,"amount":0.15,"tid":"104899229"}
        self.trade2 = ccs.btcc.public.response.Trade(self.data)

        #self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 104899229)
        self.assertEqual(self.trade2.tid(), 104899229)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 5336.46)
        self.assertEqual(self.trade2.price(), 5336.46)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.15)
        self.assertEqual(self.trade2.amount(), 0.15)

    def testType(self):
        self.assertEqual(self.trade1.type(), "undefined")
        self.assertEqual(self.trade2.type(), "undefined")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480926246)
        self.assertEqual(self.trade2.timestamp(), 1480926246)

# BTCE
#{"btc_usd":[{"type":"ask","price":753,"amount":0.133,"tid":88349995,"timestamp":1480931524},{"type":"ask","price":753,"amount":0.101,"tid":88349992,"timestamp":1480931522}]}

class Btce(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '{"btc_usd":[{"type":"ask","price":753,"amount":0.133,"tid":88349995,"timestamp":1480931524},{"type":"bid","price":753,"amount":0.101,"tid":88349992,"timestamp":1480931522}]}'
        self.trades = ccs.btce.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"type":"ask","price":753,"amount":0.133,"tid":88349995,"timestamp":1480931524}
        self.trade2 = ccs.btce.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 88349995)
        self.assertEqual(self.trade2.tid(), 88349995)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 753)
        self.assertEqual(self.trade2.price(), 753)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.133)
        self.assertEqual(self.trade2.amount(), 0.133)

    def testType(self):
        self.assertEqual(self.trade1.type(), "sell")
        self.assertEqual(self.trade2.type(), "sell")
        self.assertEqual(self.trade3.type(), "buy")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480931524)
        self.assertEqual(self.trade2.timestamp(), 1480931524)

# KRAKEN
# {"error":[],"result":{"XXBTZEUR":[["718.17700","0.26930000",1480922709.6833,"b","l",""],["718.33200","0.63766159",1480922720.8598,"b","l",""],["718.33300","0.02252948",1480922735.6065,"b","l",""] ...
# ... ,["718.43000","0.12956253",1480931987.3209,"b","m",""]],"last":"1480931987320941919"}}

class Kraken(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '{"error":[],"result":{"XXBTZEUR":[["718.17700","0.26930000",1480922709.6833,"b","l",""],["718.33200","0.63766159",1480922720.8598,"s","l",""],["718.43000","0.12956253",1480931987.3209,"b","m",""]],"last":"1480931987320941919"}}'
        self.trades = ccs.kraken.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = ["718.17700","0.26930000",1480922709.6833,"b","l",""]
        self.trade2 = ccs.kraken.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 0)
        self.assertEqual(self.trade2.tid(), 0)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 718.17700)
        self.assertEqual(self.trade2.price(), 718.17700)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.26930000)
        self.assertEqual(self.trade2.amount(), 0.26930000)

    def testType(self):
        self.assertEqual(self.trade1.type(), "buy")
        self.assertEqual(self.trade2.type(), "buy")
        self.assertEqual(self.trade3.type(), "sell")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480922709.6833)
        self.assertEqual(self.trade2.timestamp(), 1480922709.6833)

# OKCOIN
#  [{"amount":"0.123","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781524,"type":"sell"},{"amount":"0.121","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781526,"type":"sell"}]
class Okcoin(unittest.TestCase):
    def setUp(self):
        self.limit = 2

        self.json = '[{"amount":"0.123","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781524,"type":"sell"},{"amount":"0.121","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781526,"type":"buy"}]'
        self.trades = ccs.okcoin.public.response.Trades(self.json)
        self.trade1 = self.trades[0]

        self.data = {"amount":"0.123","date":1480932962,"date_ms":1480932962000,"price":"5319.00","tid":6077781524,"type":"sell"}
        self.trade2 = ccs.okcoin.public.response.Trade(self.data)

        self.trade3 = self.trades[1]

    def testTid(self):
        self.assertEqual(self.trade1.tid(), 6077781524)
        self.assertEqual(self.trade2.tid(), 6077781524)

    def testPrice(self):
        self.assertEqual(self.trade1.price(), 5319.00)
        self.assertEqual(self.trade2.price(), 5319.00)

    def testAmount(self):
        self.assertEqual(self.trade1.amount(), 0.123)
        self.assertEqual(self.trade2.amount(), 0.123)

    def testType(self):
        self.assertEqual(self.trade1.type(), "sell")
        self.assertEqual(self.trade2.type(), "sell")
        self.assertEqual(self.trade3.type(), "buy")

    def testTimestamp(self):
        self.assertEqual(self.trade1.timestamp(), 1480932962)
        self.assertEqual(self.trade2.timestamp(), 1480932962)


if __name__ == '__main__':
    unittest.main()


