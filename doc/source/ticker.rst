Ticker
======

Example of using
----------------

>>> import ccs
>>> ticker = ccs.ticker(ccs.constants.BITFINEX, ccs.constants.BTC, ccs.constants.USD)
>>> print(str(ticker))
...
>>> print(str(ticker.usymbol()))
...
>>> print(str(ticker.osymbol()))
...
>>> print(str(ticker.stock()))
...
>>> print(str(ticker.last()))
...
>>> print(str(ticker.low()))
...
>>> print(str(ticker.high()))
...
>>> print(str(ticker.ask()))
...
>>> print(str(ticker.bid()))
...
>>> print(str(ticker.volume24h()))
...
>>> print(str(ticker.timestamp()))
...
>>> print(str(ticker.dt()))


Stock argument
--------------

Currencies arguments
--------------------

Invalid
-------


Class Ticker
------------

This is description of abstract class.

.. autoclass:: ccs.abstract.Ticker
    :members:
    :inherited-members:


Mapping
-------
