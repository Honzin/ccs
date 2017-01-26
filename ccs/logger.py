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

import logging
import logging.handlers
from . import initials

def inicialization():
    name = initials.LOGGER_NAME
    format = initials.LOGGER_FORMAT
    timeformat = initials.LOGGER_TIMEFORMAT

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    removeAllHandlers(logger)
    setConsoleOutput(logger, format, timeformat)
    return logger

def removeAllHandlers(logger):
    for hdlr in logger.handlers:
        logger.removeHandler(hdlr)

def setConsoleOutput(logger, format, timeformat):
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter(format, timeformat))  ##
    logger.addHandler(ch)


