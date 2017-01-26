import unittest
import ccs

import inputs


# {"bids":[{"price":"752.91","amount":"9.6434","timestamp":"1480934403.0"}],"asks":[{"price":"753.61","amount":"7.9265","timestamp":"1480934404.0"}]}
class Bitfinex(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.bitfinex.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 756.34)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 0.49)


class Bitstamp(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.bitstamp.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 755.97)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 0.59000000)


class Btcc(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.btcc.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 5314.01)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 0.473)


class Btce(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.btce.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 752.819)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 0.0383718)

class Kraken(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.kraken.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 716.88000)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 0.212)

class Okcoin(unittest.TestCase):
    def setUp(self):
        self.limit = 2
        self.json = inputs.ORDER[self.stock]
        self.order = ccs.okcoin.public.response.Order(self.json)

    def testPrice(self):
        self.assertEqual(self.order.price(), 5315)

    def testAmount(self):
        self.assertEqual(self.order.amount(), 181.173)


if __name__ == '__main__':
    unittest.main()