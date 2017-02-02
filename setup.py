from distutils.core import setup

packages = ["ccs",
            "ccs.bitfinex",
            "ccs.bitstamp",
            "ccs.bittrex",
            "ccs.btcc",
            "ccs.btccpro",
            "ccs.btccusd",
            "ccs.btce",
            "ccs.bter",
            "ccs.cexio",
            "ccs.kraken",
            "ccs.okcoin",
            "ccs.okcoincn",
            "ccs.okcoincom",
            "ccs.poloniex"
            ]
setup(
    name            = 'ccs',
    packages        = packages,
    version         = '0.1',
    description     = 'Crypto currencies stocks (ccs) is Python package for communication with stocks which are traiding with crypto currencies. ',
    author          = 'Jan Seda',
    author_email    = 'xsedaj00@gmail.com',
    url             = 'https://github.com/Honzin/ccs',
    download_url    = 'https://github.com/Honzin/ccs/tarball/0.1',
    keywords        = ['bitfinex', 'bitstamp', 'bittrex', "btcc", "btce", "bter", "cexio", "kraken", "okcoin", "poloniex", "api", "crypto", "coin", "stock", "market"],
    classifiers     = [],
)
