import unittest
import ccs

import inputs


# {"bids":[{"price":"752.91","amount":"9.6434","timestamp":"1480934403.0"}],"asks":[{"price":"753.61","amount":"7.9265","timestamp":"1480934404.0"}]}
class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.bitfinex.public.response.Orders(self.json)

    def testLen(self):
        self.assertEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.bitfinex.public.response.Order)


# {"timestamp": "1481018631", "bids": [["755.97", "0.59000000"], ["755.92", "0.01000000"]], "asks": [["756.00", "15.38520857"], ["756.79", "13.17900000"]]}
class Bistamp(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.bitstamp.public.response.Orders(self.json)

    def testLen(self):
        self.assertEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.bitstamp.public.response.Order)


# {"asks":[[5314.01,0.473],[5313.31,0.4639]],"bids":[[5313.12,0.1525],[5313.11,0.001]],"date":1481018947}
class Btcc(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.btcc.public.response.Orders(self.json)

    def testLen(self):
        self.assertEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.btcc.public.response.Order)

# {"btc_usd":{"asks":[[752.819,0.0383718],[752.82,0.09885703]],"bids":[[751.611,0.5616282],[751.61,50]]}}
class Btce(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.btce.public.response.Orders(self.json)

    def testLen(self):
        self.assertAlmostEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.btce.public.response.Order)

# {"error":[],"result":{"XXBTZEUR":{"asks":[["716.88000","0.212",1481019303],["716.88100","21.719",1481019298]],"bids":[["715.20300","0.089",1481019301],["715.20200","1.720",1481019303]]}}}
class Kraken(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.kraken.public.response.Orders(self.json)

    def testLen(self):
        self.assertEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.kraken.public.response.Order)


# {"asks":[[5315,181.173],[5314,12.358]],"bids":[[5313,13.873],[5312,13.775]]}
class Okcoin(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERS[self.stock]
        self.orders = ccs.okcoin.public.response.Orders(self.json)

    def testLen(self):
        self.assertEqual(len(self.orders), self.limit)

    def testGetItem(self):
        self.assertIsInstance(self.orders[0], ccs.okcoin.public.response.Order)


if __name__ == '__main__':
    unittest.main()