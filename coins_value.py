"""
Here you find a simple web scrapping to find values on HTML code of 'dolarhoje'
"""

from urllib.request import urlopen


def coins_value():
    coins = [
        "1 Dólar Americano",
        "1 Dólar Australiano",
        "1 Dólar Canadense",
        "1 Dólar Neozelandês",
        "1 Franco Suíço",
        "1 Libra",
        "1 Euro",
        "1 Peso Argentino",
        "1 Peso Mexicano",
        "1 Peso Uruguáio",
        "1 Rublo Russo",
        "1 Yuan"
    ]

    links = ["https://dolarhoje.com/",
             "https://dolarhoje.com/dolar-australiano-hoje/",
             "https://dolarhoje.com/dolar-canadense-hoje/",
             "https://dolarhoje.com/dolar-neozelandes-hoje/",
             "https://dolarhoje.com/franco-suico-hoje/",
             "https://dolarhoje.com/libra-hoje/",
             "https://dolarhoje.com/euro-hoje/",
             "https://dolarhoje.com/peso-argentino/",
             "https://dolarhoje.com/peso-mexicano-hoje/",
             "https://dolarhoje.com/peso-uruguaio/",
             "https://dolarhoje.com/rublo-russo-hoje/",
             "https://dolarhoje.com/yuan-hoje/"
             ]

    prices = []

    for link in links:
        html_code = urlopen(link).read().decode("utf-8")
        html_code = html_code.split(' ')

        count = 0
        for values in html_code:
            if 'value' in values:
                count += 1
                prices.append(values)

            if count == 2:
                break

    string = ''
    count = 0
    for coin in coins:
        string += coin
        string += ' = '
        string += prices[count+1][7:11]
        string += ' Reais'
        string += '\n'

        count += 2

    return string


def digital_coins_value():
    coins = [
        "1 Bitcoin",
        "1 Binance Coin",
        "1 Bitcoin Diamond",
        "1 Bitcoin Cash",
        "1 Bitcoin Gold",
        "1 Bitcoin SV",
        "1 Dash",
        "1 Decred",
        "1 Denta Coin",
        "1 Ethereum",
        "1 EOS",
        "1 Ethereum Classic",
        "1 Lisk",
        "1 Litecoin",
        "1 Monero",
        "1 Nano",
        "1 Pundi X"
    ]

    links = ["https://dolarhoje.com/bitcoin-hoje/",
             "https://dolarhoje.com/binance-coin-hoje/",
             "https://dolarhoje.com/bitcoin-diamond-hoje/",
             "https://dolarhoje.com/bitcoin-cash-hoje/",
             "https://dolarhoje.com/bitcoin-gold-hoje/",
             "https://dolarhoje.com/bitcoin-sv-hoje/",
             "https://dolarhoje.com/dash/",
             "https://dolarhoje.com/decred/",
             "https://dolarhoje.com/dentacoin-hoje/",
             "https://dolarhoje.com/ethereum/",
             "https://dolarhoje.com/eos-hoje/",
             "https://dolarhoje.com/ethereum-classic-hoje/",
             "https://dolarhoje.com/lisk/",
             "https://dolarhoje.com/litecoin/",
             "https://dolarhoje.com/monero/",
             "https://dolarhoje.com/nano-hoje/",
             "https://dolarhoje.com/pundi-x-hoje/"
             ]

    coins2 = [
        "1 Aeternity",
        "1 Ark",
        "1 Basic Attetion Token",
        "1 Bitshares",
        "1 Bytom",
        "1 Cardano",
        "1 Digibyte",
        "1 Dogecoin",
        "1 Electroneum",
        "1 Golem",
        "1 Icon",
        "1 Iota",
        "1 Komodo",
        "1 NEM",
        "1 Ontology",
        "1 ReddCoin",
        "1 Ripple XRP",
        "1 SALT",
        "1 SiaCoin"
        "1 Status",
        "1 Steem",
        "1 Stellar Lumens",
        "1 Tether",
        "1 TRON",
        "1 TrueUSD",
        "1 USD Coin",
        "1 VeChain",
        "1 Verge",
        "1 Wanchain",
        "1 Zilliqa",
        "1 0x"
    ]

    links2 = [
        "https://dolarhoje.com/aeternity-hoje/",
        "https://dolarhoje.com/ark-hoje/",
        "https://dolarhoje.com/basic-attention-token-hoje/",
        "https://dolarhoje.com/bitshares-hoje/",
        "https://dolarhoje.com/bytom-hoje/",
        "https://dolarhoje.com/cardano-hoje/",
        "https://dolarhoje.com/digibyte-hoje/",
        "https://dolarhoje.com/dogecoin-hoje/",
        "https://dolarhoje.com/electroneum-hoje/",
        "https://dolarhoje.com/golem-hoje/",
        "https://dolarhoje.com/icon-hoje/",
        "https://dolarhoje.com/iota/",
        "https://dolarhoje.com/komodo-hoje/",
        "https://dolarhoje.com/nem/",
        "https://dolarhoje.com/ontology-hoje/",
        "https://dolarhoje.com/reddcoin-hoje/",
        "https://dolarhoje.com/ripple-hoje/",
        "https://dolarhoje.com/salt-hoje/",
        "https://dolarhoje.com/siacoin-hoje/",
        "https://dolarhoje.com/status-hoje/",
        "https://dolarhoje.com/steem-hoje/",
        "https://dolarhoje.com/stellar-lumens-hoje/",
        "https://dolarhoje.com/tether-hoje/",
        "https://dolarhoje.com/tron-hoje/",
        "https://dolarhoje.com/trueusd-hoje/",
        "https://dolarhoje.com/usd-coin-hoje/",
        "https://dolarhoje.com/vechain-hoje/",
        "https://dolarhoje.com/verge-hoje/",
        "https://dolarhoje.com/wanchain-hoje/",
        "https://dolarhoje.com/zilliqa-hoje/",
        "https://dolarhoje.com/0x-hoje/"
    ]

    prices = []

    for link in links:
        html_code = urlopen(link).read().decode("utf-8")
        html_code = html_code.split(' ')

        count = 0
        for values in html_code:
            if 'value' in values:
                count += 1
                prices.append(values)

            if count == 2:
                break

    string = ''
    count = 0
    for coin in coins:
        if coin == "1 Bitcoin":
            end = 16

        elif coin == "1 Ethereum" or coin == "1 Denta Coin":
            end = 15

        elif coin == "1 Binance Coin" or coin == "1 Bitcoin Cash" or coin == "1 Monero" or coin == "1 Pundi X":
            end = 14

        elif coin == "1 Bitcoin Diamond" or coin == "1 EOS" or coin == "1 Nano":
            end = 12

        elif coin == "1 Lisk":
            end = 11

        else:
            end = 13

        string += coin
        string += ' = '
        string += prices[count+1][7:end]
        string += ' Reais'
        string += '\n'

        count += 2

    prices = []

    for link in links2:
        html_code = urlopen(link).read().decode("utf-8")
        html_code = html_code.split(' ')

        count = 0
        for values in html_code:
            if 'value' in values:
                count += 1
                prices.append(values)

            if count == 2:
                break

    count = 0
    for coin in coins2:
        string += coin
        string += ' = '
        string += prices[count + 1][7:11]
        string += ' Reais'
        string += '\n'

        count += 2

    return string
