import requests
 

def get_coin_prices(coins, currencies):
    coin = ",".join(coins)
    currency = ",".join(currencies)

    COINGECKO_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    data = requests.get(COINGECKO_URL).json()

    return data