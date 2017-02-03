import unittest
import ccs
import jsonschema
import json
import time

class Valid(unittest.TestCase):
    def setUp(self):
        # Kraken doenst work with all pairs which it return om request getTradablePairs()
        self.pairs = ['XZECZUSD',
                        'XLTCZUSD',
                        'XETCXXBT',
                        'XETHZEUR',
                        'XICNXETH',
                        'XREPZEUR',
                        'XETCZUSD',
                        'XXRPXXBT',
                        'XETCXETH',
                        'XXBTZGBP',
                        'XETHZUSD',
                        'XLTCZEUR',
                        'XETHZCAD',
                        'XXBTZJPY',
                        'XETHZJPY',
                        'XICNXXBT',
                        'XXLMXXBT',
                        'XXDGXXBT',
                        'XREPXETH',
                        'XETCZEUR',
                        'XREPZUSD',
                        'XZECXXBT',
                        'XETHXXBT',
                        'XLTCXXBT',
                        'XXBTZCAD',
                        'XXBTZEUR',
                        'XETHZGBP',
                        'XXBTZUSD',
                        'XREPXXBT',
                        'XZECZEUR',
                        ]

        self.alt_pairs = [
                        'LTCXBT',
                        'XLMXBT',
                        'REPUSD',
                        'ETCEUR',
                        'ETHGBP',
                        'ETHUSD',
                        'ETHCAD',
                        'XBTUSD',
                        'ICNETH',
                        'XBTEUR',
                        'REPXBT',
                        'REPEUR',
                        'ETHEUR',
                        'ZECEUR',
                        'REPETH',
                        'XBTGBP',
                        'LTCUSD',
                        'ETHJPY',
                        'ETCXBT',
                        'ETCETH',
                        'ICNXBT',
                        'XBTCAD',
                        'ETHXBT',
                        'ETCUSD',
                        'ZECXBT',
                        'XDGXBT',
                        'XRPXBT',
                        'ZECUSD',
                        'XBTJPY',
                        'LTCEUR',
                        ]

        time.sleep(2)

        self.schema = ccs.kraken.configuration.SCHEMA["getAssetInfo"]
        self.pair = "XXBTZEUR"

    def testSchema(self):
        r = ccs.kraken.public.getAssetInfo()
        jsonschema.validate(json.loads(r), self.schema)

    def testInfo(self):
        r = ccs.kraken.public.getAssetInfo(info="info")
        jsonschema.validate(json.loads(r), self.schema)

    def testAsset(self):
        r = ccs.kraken.public.getAssetInfo(asset="XXBT")
        jsonschema.validate(json.loads(r), self.schema)

    def testAssetArray(self):
        r = ccs.kraken.public.getAssetInfo(asset="XXBT,ZEUR")
        jsonschema.validate(json.loads(r), self.schema)

    def testAclass(self):
        r = ccs.kraken.public.getAssetInfo(aclass="currency")
        jsonschema.validate(json.loads(r), self.schema)

    def testInfoAssetAclass(self):
        r = ccs.kraken.public.getAssetInfo(info="info", asset="XXBT,ZEUR", aclass="currency")
        jsonschema.validate(json.loads(r), self.schema)



    # def testPairs(self):
    #     for pair in self.pairs:
    #         r = ccs.kraken.public.getTradableAssetPairs()
    #         jsonschema.validate(json.loads(r), self.schema)
    #         time.sleep(7)
    #
    # def testAltPairs(self):
    #     for pair in self.pairs:
    #         r = ccs.kraken.public.getRecentTrades(pair)
    #         jsonschema.validate(json.loads(r), self.schema)
    #         time.sleep(7)




# class Invalid(unittest.TestCase):
#     def setUp(self):
#         self.fail_symbol = "abcdef"
#         self.schema = ccs.kraken.configuration.SCHEMA["getTradableAssetPairs"]
#
#     def testPair(self):
#         with self.assertRaises(jsonschema.exceptions.ValidationError):
#             r = ccs.kraken.public.getTradableAssetPairs()
#             jsonschema.validate(json.loads(r), self.schema)



if __name__ == '__main__':
    unittest.main()


