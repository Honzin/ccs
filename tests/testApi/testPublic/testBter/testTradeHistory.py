# -*- coding: utf8 -*-

"""
This file implements test cases for validation communication with REST endpoint on Bter. This endpoint offer informations about trades.
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
    return ccs.bter.configuration.SCHEMA["tradeHistory"]


def sleep():
    time.sleep(3)


class Valid(unittest.TestCase):
    def setUp(self):
        self.symbols = ["btc_cny", "ltc_cny", "blk_cny", "bitcny_cny", "bqc_cny", "btb_cny", "btq_cny", "bts_cny", "cent_cny", "cmc_cny", "cnc_cny", "rep_cny",
                        "dgc_cny", "doge_cny", "dash_cny", "dtc_cny", "dvc_cny", "eth_cny", "etc_cny", "exc_cny", "ftc_cny", "frc_cny", "ifc_cny", "max_cny",
                        "mec_cny", "mint_cny", "mmc_cny", "nbt_cny", "net_cny", "nmc_cny", "nxt_cny", "ppc_cny", "pts_cny", "qrk_cny", "red_cny", "shell_cny",
                        "src_cny", "tag_cny", "tbc_cny", "tips_cny", "tix_cny", "vrc_cny", "vtc_cny", "wdc_cny", "xcp_cny", "xmr_cny", "xpm_cny", "xtc_cny",
                        "yac_cny", "zcc_cny", "zet_cny", "btc_usd", "bitusd_usd", "ltc_usd", "doge_usd", "dash_usd", "nxt_usd", "xcp_usd", "bts_usd", "ltc_btc",
                        "ac_btc", "arch_btc", "aur_btc", "bay_btc", "bbr_btc", "blk_btc", "bitgld_btc", "block_btc", "bqc_btc", "btb_btc", "btcd_btc", "bts_btc",
                        "buk_btc", "c2_btc", "cdc_btc", "ckc_btc", "comm_btc", "cmc_btc", "cnc_btc", "rep_btc", "hkg_btc", "dgc_btc", "doge_btc", "dns_btc",
                        "dash_btc", "drkc_btc", "dtc_btc", "eth_btc", "etc_btc", "exc_btc", "flt_btc", "frc_btc", "frsh_btc", "ftc_btc", "ftp_btc", "gemz_btc",
                        "ghost_btc", "gml_btc", "kdc_btc", "lts_btc", "max_btc", "mec_btc", "mint_btc", "mmc_btc", "msc_btc", "nav_btc", "nbt_btc", "nsr_btc",
                        "nec_btc", "nmc_btc", "node_btc", "nas_btc", "net_btc", "nfd_btc", "nxt_btc", "ntx_btc", "ppc_btc", "prt_btc", "pts_btc", "qrk_btc", "rox_btc",
                        "sfr_btc", "slm_btc", "spark_btc", "src_btc", "swift_btc", "tag_btc", "tbc_btc", "xtc_btc", "yac_btc", "via_btc", "vrc_btc", "vtc_btc",
                        "wdc_btc", "xc_btc", "xch_btc", "xcn_btc", "xcr_btc", "xcp_btc", "xem_btc", "xpm_btc", "xmr_btc", "qora_btc", "zcc_btc", "zet_btc", "ctc_btc",
                        "mg_btc", "cent_ltc", "dvc_ltc", "ifc_ltc", "net_ltc", "nfd_ltc", "red_ltc", "tips_ltc", "tix_ltc", "etc_eth", "zec_btc", "zec_cny",
                        "bts_nxt", "xcp_nxt", "btcd_nxt", "btc_bitusd", "mgw_btc", "nxtty_btc", "atomic_btc", "mrkt_btc", "nxtty_cny", "token_btc", "token_nxt",
                        "token_cny", "token_btcd", "unity_btc", "unity_nxt", "unity_cny", "dice_btc", "dice_nxt"]

        self.symbol = self.symbols[0]

        sleep()

    def testSchema(self):
        r = ccs.bter.public.tradeHistory(self.symbol)
        jsonschema.validate(json.loads(r), schema())

    @unittest.skip("time-consuming")
    def testSymbols(self):
        for symbol in self.symbols:
            r = ccs.bter.public.tradeHistory(symbol)
            jsonschema.validate(json.loads(r), schema())
            sleep()


class Invalid(unittest.TestCase):
    def setUp(self):
        self.symbol = "aaa_bbb"

    def testResponse(self):
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            r = ccs.bter.public.tradeHistory(self.symbol)
            jsonschema.validate(json.loads(r), schema())


if __name__ == '__main__':
    unittest.main()
