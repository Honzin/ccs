Kraken
======

API call rate limit

Every user of our API has a "call counter" which starts at 0.

Ledger/trade history calls increase the counter by 2.

Place/cancel order calls do not affect the counter.

All other API calls increase the counter by 1.

The user's counter is reduced every couple of seconds, and if the counter exceeds the user's maximum API access is suspended for 15 minutes. Tier 2 users have a maximum of 15 and their count gets reduced by 1 every 3 seconds.


.. currentmodule:: ccs.kraken.public

Asset info
----------
.. autofunction:: getAssetInfo


Asset pairs
-----------
.. autofunction:: getTradableAssetPairs

OHLC
----
.. autofunction:: getOHLCdata

Orderbook
---------
.. autofunction:: getOrderBook


Ticker
------
.. autofunction:: getTickerInformation

Trades
------
.. autofunction:: getRecentTrades

Server time
-----------
.. autofunction:: getServerTime

Spread
------
.. autofunction:: getRecentSpreadData


