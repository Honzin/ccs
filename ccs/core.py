# -*- coding: utf8 -*-

# TODO
"""
...
"""

__author__ = "Jan Seda"
__copyright__ = "Copyright (C) Jan Seda"
__credits__ = []
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Jan Seda"
__email__ = ""
__status__ = "Production"

import http.client
import zlib
from . import constants
from . import initials
import logging

import importlib

def get(hostname, request, header, compression, timeout):
    header['Accept-Encoding'] = compression
    con = http.client.HTTPSConnection(hostname, timeout=timeout)
    con.request(constants.GET, request, "", header)
    response = con.getresponse()
    data = decompress(response.read(), compression, header['Accept-Charset'])
    con.close()

    logger = logging.getLogger(logerName())

    # TODO
    # vyhodit - predelat
    if verbose():
        logger.debug(constants.DELIMITER)
        logger.debug("REQUEST ")
        logger.debug("Method: GET ")
        logger.debug("Hostname: " + str(hostname))
        logger.debug("Request: " + str(request))
        logger.debug("HTTP head: " + str(header))
        logger.debug("")
        logger.debug("RESPONSE ")
        logger.debug("JSON: " + str(data))
        logger.debug(constants.DELIMITER)

    return data

# TODO COPY LIKE HELL
def post(hostname, request, header, compression, timeout, params):
    header['Accept-Encoding'] = compression
    con = http.client.HTTPSConnection(hostname, timeout=timeout)
    con.request(constants.POST, request, params , header)
    response = con.getresponse()
    data = decompress(response.read(), compression, header['Accept-Charset'])
    con.close()

    logger = logging.getLogger(logerName())

    # TODO
    # vyhodit - predelat
    if verbose():
        logger.debug(constants.DELIMITER)
        logger.debug("REQUEST ")
        logger.debug("Method: GET ")
        logger.debug("Hostname: " + str(hostname))
        logger.debug("Request: " + str(request))
        logger.debug("HTTP head: " + str(header))
        logger.debug("")
        logger.debug("RESPONSE ")
        logger.debug("JSON: " + str(data))
        logger.debug(constants.DELIMITER)

    return data


def decompress(data, compression, charset):
    if compression == constants.GZIP:
        return zlib.decompress(data, zlib.MAX_WBITS + 16).decode(charset)
    if compression == constants.DEFLATE:
        return zlib.decompress(data, -zlib.MAX_WBITS).decode(charset)
    if compression == constants.IDENTITY:
        return data.decode(charset)


# TODO
# PROCE TO NENI POD Configuration

# s = stock
# s = stock
def compression(s):
    cfg = Configuration()
    return cfg.compressions[s]

# def charset(s):
#     cfg = Configuration()
#     return cfg.charsets[s]

def timeout(s):
    cfg = Configuration()
    return cfg.timeouts[s]

def hostname(s):
    cfg = Configuration()
    return cfg.hostnames[s]

def request(s, r):
    cfg = Configuration()
    return cfg.requests[s][r]

def header(s):
    cfg = Configuration()
    return cfg.headers[s]

def verbose():
    cfg = Configuration()
    return cfg.verbose

def logerName():
    cfg = Configuration()
    return cfg.logger_name

def raw():
    cfg = Configuration()
    return cfg.raw


# Borg
# http://stackoverflow.com/questions/1318406/why-is-the-borg-pattern-better-than-the-singleton-pattern-in-python
class Configuration:

    _shared_state = {}

    def __new__(cls, *args, ** kwargs):
        obj = super(Configuration, cls).__new__(cls, *args, ** kwargs)
        obj.__dict__ = cls._shared_state
        return obj

    def __init__(self):
        self.headers = {}
        self.hostnames = {}
        self.compressions = {}
        self.requests = {}
        self.timeouts = {}
        self.mapping = {}
        self.schema = {}

        self.verbose = initials.VERBOSE
        self.logger_name = initials.LOGGER_NAME
        self.raw = initials.RAW

        self.append(constants.BITFINEX)
        self.append(constants.BITSTAMP)
        self.append(constants.BITTREX)
        self.append(constants.BTCC)
        self.append(constants.BTCCPRO)
        self.append(constants.BTCCUSD)
        self.append(constants.BTCE)
        self.append(constants.BTER)
        self.append(constants.CEXIO)
        self.append(constants.KRAKEN)
        self.append(constants.POLONIEX)

        # self.append(constants.BITKONAN)
        # self.append(constants.COINFLOOR)
        # self.append(constants.BITBAY)
        # self.append(constants.EXMO)
        # self.append(constants.HITBTC)
        # self.append(constants.ITBIT)
        # self.append(constants.THEROCKTRAIDING)
        # self.append(constants.FYBSE)
        # self.append(constants.FYBSG)
        self.append(constants.OKCOINCOM)
        self.append(constants.OKCOINCN)
        # self.append(constants.CAMPBX)
        # self.append(constants.HUOBI)
        # self.append(constants.LOCALBITCOINS)
        # self.append(constants.BTCMARKETS)
        # self.append(constants.MERCADOBITCOIN)
        # self.append(constants.BIT2C)
        # self.append(constants.BITNZ)
        # self.append(constants.BITMARKET)
        # self.append(constants.LAKEBTC)

    def append(self, stock):
        # TODO
        # try to find clean way how to do it
        m = importlib.import_module("ccs." + stock + "." + "configuration", package=None)
        c = m.__dict__
        # c = eval(stock + ".configuration.__dict__")
        self.headers[stock] =      c[constants.HEADER.upper()]
        self.hostnames[stock] =    c[constants.HOSTNAME.upper()]
        self.compressions[stock] = c[constants.COMPRESSION.upper()]
        self.requests[stock] =     c[constants.REQUESTS.upper()]
        self.timeouts[stock] =     c[constants.TIMEOUT.upper()]
        self.mapping[stock] =      c[constants.MAPPING.upper()]
        self.schema[stock] =       c[constants.SCHEMA.upper()]
