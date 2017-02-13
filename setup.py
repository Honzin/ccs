from distutils.core import setup

packages = ["ccs",
            "ccs.bitfinex",
            "ccs.bitfinex.public",
            "ccs.bitstamp",
            "ccs.bitstamp.public",
            "ccs.bittrex",
            "ccs.bittrex.public",
            "ccs.btcc",
            "ccs.btcc.public",
            "ccs.btccpro",
            "ccs.btccpro.public",
            "ccs.btccusd",
            "ccs.btccusd.public",
            "ccs.btce",
            "ccs.btce.public",
            "ccs.bter",
            "ccs.bter.public",
            "ccs.cexio",
            "ccs.cexio.public",
            "ccs.kraken",
            "ccs.kraken.public",
            "ccs.okcoin",
            "ccs.okcoin.public",
            "ccs.okcoincn",
            "ccs.okcoincn.public",
            "ccs.okcoincom",
            "ccs.okcoincom.public",
            "ccs.poloniex",
            "ccs.poloniex.public"
            ]

classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    # 'Topic :: Software Development :: Build Tools',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name            = 'ccs',
    packages        = packages,
    version         = '0.1.9',
    description     = 'Crypto currencies stocks (ccs) is Python package for communication with stocks which are traiding with crypto currencies. Documentation is placed  http://cryptocurrenciesstocks.readthedocs.io',
    author          = 'Jan Seda',
    author_email    = 'xsedaj00@gmail.com',
    url             = 'https://github.com/Honzin/ccs',
    download_url    = 'https://github.com/Honzin/ccs/tarball/0.1.9',
    install_requires=["jsonschema"],
    keywords        = ['bitfinex', 'bitstamp', 'bittrex', "btcc", "btce", "bter", "cexio", "kraken", "okcoin", "poloniex", "api", "crypto", "coin", "stock", "market", "unification"],
    classifiers     = classifiers,
)
