# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Bittrex. This endpoint offer informations about trades.
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"


import unittest
import ccs
import jsonschema
import json
import time


def schema():
    return ccs.bittrex.configuration.SCHEMA["getMarketHistory"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self. markets = ['BTC-LTC', 'BTC-DOGE', 'BTC-VTC', 'BTC-PPC', 'BTC-FTC', 'BTC-RDD', 'BTC-NXT', 'BTC-DASH', 'BTC-POT', 'BTC-BLK', 'BTC-EMC2', 'BTC-MYR', 'BTC-AUR', 'BTC-UTC', 'BTC-MZC', 'BTC-EFL',
                         'BTC-GLD', 'BTC-SLR', 'BTC-PTC', 'BTC-GRS', 'BTC-NLG', 'BTC-RBY', 'BTC-XWC', 'BTC-MONA', 'BTC-BITS', 'BTC-THC', 'BTC-ENRG', 'BTC-ERC', 'BTC-NAUT', 'BTC-VRC', 'BTC-CURE', 'BTC-BLC',
                         'BTC-XC', 'BTC-BBR', 'BTC-HYPER', 'BTC-CCN', 'BTC-XMR', 'BTC-CLOAK', 'BTC-START', 'BTC-KORE', 'BTC-XDN', 'BTC-TRK', 'BTC-QTL', 'BTC-TRUST', 'BTC-NAV', 'BTC-XST', 'BTC-BTCD', 'BTC-VIA',
                         'BTC-UNO', 'BTC-PINK', 'BTC-IOC', 'BTC-SDC', 'BTC-LXC', 'BTC-CANN', 'BTC-FC2', 'BTC-J', 'BTC-SYS', 'BTC-NEOS', 'BTC-DGB', 'BTC-JBS', 'BTC-BSTY', 'BTC-BURST', 'BTC-PXI', 'BTC-DGC',
                         'BTC-SLG', 'BTC-STV', 'BTC-EXCL', 'BTC-SWIFT', 'BTC-ARCH', 'BTC-NET', 'BTC-GHC', 'BTC-DOPE', 'BTC-BLOCK', 'BTC-ABY', 'BTC-BYC', 'BTC-XMG', 'BTC-XQN', 'BTC-BLITZ', 'BTC-VPN', 'BTC-BAY',
                         'BTC-BTS', 'BTC-FAIR', 'BTC-METAL', 'BTC-SPR', 'BTC-VTR', 'BTC-XRP', 'BTC-GAME', 'BTC-GP', 'BTC-COVAL', 'BTC-NXS', 'BTC-XCP', 'BTC-SJCX', 'BTC-BITB', 'BTC-HZ', 'BTC-GEO', 'BTC-FLDC',
                         'BTC-WBB', 'BTC-GEMZ', 'BTC-GRC', 'BTC-XCO', 'BTC-MTR', 'BTC-FLO', 'BTC-U', 'BTC-NBT', 'BTC-MUE', 'BTC-XEM', 'BTC-8BIT', 'BTC-CLAM', 'BTC-NTRN', 'BTC-SLING', 'BTC-DMD', 'BTC-GAM',
                         'BTC-UNIT', 'BTC-GRT', 'BTC-VIRAL', 'BTC-SPHR', 'BTC-ARB', 'BTC-OK', 'BTC-SNRG', 'BTC-PKB', 'BTC-TES', 'BTC-CPC', 'BTC-AEON', 'BTC-ETH', 'BTC-GCR', 'BTC-TX', 'BTC-BCY', 'BTC-EXP',
                         'BTC-NEU', 'BTC-SWING', 'BTC-INFX', 'BTC-SOIL', 'BTC-OMNI', 'BTC-AMP', 'BTC-AGRS', 'BTC-XLM', 'BTC-BTA', 'BTC-MEC', 'USDT-BTC', 'BITCNY-BTC', 'BTC-SCRT', 'BTC-SCOT', 'BTC-CLUB',
                         'BTC-VOX', 'BTC-EMC', 'BTC-FCT', 'BTC-MAID', 'BTC-FRK', 'BTC-EGC', 'BTC-SLS', 'BTC-ORB', 'BTC-RADS', 'BTC-DCR', 'BTC-SEC', 'BTC-BSD', 'BTC-XVG', 'BTC-DNET', 'BTC-WARP', 'BTC-XVC',
                         'BTC-MEME', 'BTC-DES', 'BTC-SAR', 'BTC-STEEM', 'BTC-2GIVE', 'BTC-LSK', 'BTC-KR', 'BTC-PDC', 'BTC-BRK', 'BTC-DGD', 'ETH-DGD', 'BTC-WAVES', 'BTC-RISE', 'BTC-LBC', 'BTC-SBD', 'BTC-BRX',
                         'BTC-DRACO', 'BTC-UNIQ', 'BTC-ETC', 'ETH-ETC', 'BTC-STRAT', 'BTC-UNB', 'BTC-SYNX', 'BTC-TRIG', 'BTC-EBST', 'BTC-VRM', 'BTC-SLK', 'BTC-XAUR', 'BTC-SNGLS', 'BTC-JWL', 'BTC-REP', 'BTC-SHIFT',
                         'BTC-ARDR', 'BTC-XZC', 'BTC-ANS', 'BTC-ZEC', 'BTC-ZCL', 'BTC-MEGA', 'BTC-IOP', 'BTC-DAR']

        self.market = self.markets[0]

        sleep()

    def testSchema(self):
        r = ccs.bittrex.public.getMarketHistory(self.market)
        jsonschema.validate(json.loads(r), schema())

    @unittest.skip("time-consuming")
    def testCurrencies(self):
        for market in self.markets:
            r = ccs.bittrex.public.getMarketHistory(market)
            jsonschema.validate(json.loads(r), schema())
            sleep()

    @unittest.skip("server ignore this parametr")
    def testCount(self):
        count = 10
        r = ccs.bittrex.public.getMarketHistory(self.market, count=count)
        d = json.loads(r)
        jsonschema.validate(d, schema())

        self.assertLessEqual(len(d["result"]), count)


class Invalid(unittest.TestCase):
    def setUp(self):
        self.market = "aaa-bbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bittrex.public.getMarketHistory(self.market)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
