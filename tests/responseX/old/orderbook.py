import unittest
import ccs

import inputs

class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.bitfinex.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.bitfinex.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.bitfinex.public.response.Orders)


class Bitstamp(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.bitstamp.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.bitstamp.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.bitstamp.public.response.Orders)
        
class Btcc(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.btcc.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.btcc.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.btcc.public.response.Orders)


class Btce(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.btce.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.btce.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.btce.public.response.Orders)


class Kraken(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.kraken.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.kraken.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.kraken.public.response.Orders)


class Okcoin(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDERBOOK[self.stock]
        self.orderbook = ccs.okcoin.public.response.OrderBook(self.json)

    def testAsks(self):
        self.assertIsInstance(self.orderbook.asks(), ccs.okcoin.public.response.Orders)

    def testBids(self):
        self.assertIsInstance(self.orderbook.bids(), ccs.okcoin.public.response.Orders)

if __name__ == '__main__':
    unittest.main()