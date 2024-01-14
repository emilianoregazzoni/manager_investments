# Manager investments
Cli command developed in Python, using SQLAlchemy and CoinGecko API to manage the investments of portfolios getting live information about cryptocurrencies

## __Python, SQLAlchemy and Coingecko__  

In this project I worked with Python, SQLAlchemy and Coingecko API to develop a simple Cli console to manage investments and portfolios of clients.
First of all I installed SQLAlchemy to work with a SQLLite database locally:

`pip install sqlalchemy`

Then I got into Coingecko website and explore the endpoints until I got the public API to get the info. 
Then I created a function to got the information of the coins and currencies:


```
import requests

def get_coin_prices(coins, currencies):

    coin = ",".join(coins)
    currency = ",".join(currencies)
    COINGECKO_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    data = requests.get(COINGECKO_URL).json()

   return data
```
