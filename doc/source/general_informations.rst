General informations
====================

Handeling exceptions
--------------------

Each description of function contains example of using. These examples are without exceptions treatment. Here is example for right using of :func:`~ccs.bitstamp.public.ticker`.

>>> import ccs
>>> response = ""
>>> try:
>>>     response = ccs.bitstamp.public.ticker("btcusd")
>>> except:
>>>     # handle exception
>>>     pass

How it wokrs
------------

These functions are only python wrappers around get requests. It means that here are not any extra controls parametres. Parametres which will give are strictly coding to GET request. It makes this functions flexible for changes. Typical situation it can be adding new symbol.
On the other hand it mean you can write something like this:

>>> import ccs
>>> ccs.bitstamp.public.transactions("btcusd", time="abcd")

It is clear that value of timestamp is not valid. However code doesnt invoke any exception. In fact it will return valid list of trades. But this behavior depends on Bitfinex server.

Response validation
-------------------

If you would like validate response form server you can use prepared  json schemas for validation. Here are examples for ticker method.

>>> import ccs
>>> import json
>>> import jsonschema
>>>
>>> try:
>>>     response = ccs.bitstamp.public.ticker("btcusd")
>>>     schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["ticker"]
>>>     jsonschema.validate(json.loads(response), schema)
>>> except jsonschema.exceptions.ValidationError:
>>>     # handle validation exception
>>>     pass
>>> except:
>>>     # handle rest of exceptions (communication, ...)
>>>     pass

Keys of schemas are absolutely same like name of functions. Schema of transaction request it can be read:

>>> schema = ccs.cfg.schema[ccs.constants.BITSTAMP]["transactions"]

Validation is not buil in function. The reason is bigger flexibility. It can happen that stock will change schema of json but API will stay same. For this and other situations validation is not implicit on this module level.

Congestion control
------------------

Last information is recommandation. These functions do not offer protection against congestion. It means you or your IP can be banned if you will send your requests very often. Send your requests in reasonable period. In fact here is not good reason ask every second on history of transactions, because stock with crypto currencies are not so liquid (without some Chinese stocks).


