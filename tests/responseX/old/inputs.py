import ccs

ORDERS = {}
ORDERS[ccs.constants.BITFINEX] = [{"price":"756.34","amount":"0.49","timestamp":"1481018173.0"},{"price":"756.32","amount":"0.0480676","timestamp":"1481018159.0"}]
ORDERS[ccs.constants.BITSTAMP] = [["755.97", "0.59000000"], ["755.92", "0.01000000"]]
ORDERS[ccs.constants.BTCC] = [[5314.01,0.473],[5313.31,0.4639]]
ORDERS[ccs.constants.BTCE] = [[752.819,0.0383718],[752.82,0.09885703]]
ORDERS[ccs.constants.KRAKEN] = [["716.88000","0.212",1481019303],["716.88100","21.719",1481019298]]
ORDERS[ccs.constants.OKCOIN] = [[5315,181.173],[5314,12.358]]

ORDERBOOK = {}
ORDERBOOK[ccs.constants.BITFINEX] = '{"bids":[{"price":"752.91","amount":"9.6434","timestamp":"1480934403.0"}],"asks":[{"price":"753.61","amount":"7.9265","timestamp":"1480934404.0"}]}'
ORDERBOOK[ccs.constants.BITSTAMP] = '{"timestamp": "1481018631", "bids": [["755.97", "0.59000000"], ["755.92", "0.01000000"]], "asks": [["756.00", "15.38520857"], ["756.79", "13.17900000"]]}'
ORDERBOOK[ccs.constants.BTCC] = '{"asks":[[5314.01,0.473],[5313.31,0.4639]],"bids":[[5313.12,0.1525],[5313.11,0.001]],"date":1481018947}'
ORDERBOOK[ccs.constants.BTCE] = '{"btc_usd":{"asks":[[752.819,0.0383718],[752.82,0.09885703]],"bids":[[751.611,0.5616282],[751.61,50]]}}'
ORDERBOOK[ccs.constants.KRAKEN] = '{"error":[],"result":{"XXBTZEUR":{"asks":[["716.88000","0.212",1481019303],["716.88100","21.719",1481019298]],"bids":[["715.20300","0.089",1481019301],["715.20200","1.720",1481019303]]}}}'
ORDERBOOK[ccs.constants.OKCOIN] = '{"asks":[[5315,181.173],[5314,12.358]],"bids":[[5313,13.873],[5312,13.775]]}'

ORDER = {}
ORDER[ccs.constants.BITFINEX] = {"price":"756.34","amount":"0.49","timestamp":"1481018173.0"}
ORDER[ccs.constants.BITSTAMP] = ["755.97", "0.59000000"]
ORDER[ccs.constants.BTCC] = [5314.01,0.473]
ORDER[ccs.constants.BTCE] = [752.819,0.0383718]
ORDER[ccs.constants.KRAKEN] = ["716.88000","0.212",1481019303]
ORDER[ccs.constants.OKCOIN] = [5315,181.173]