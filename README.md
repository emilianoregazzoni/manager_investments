# Manager investments :moneybag:
Cli command developed in Python, using SQLAlchemy and CoinGecko API to manage the investments of portfolios getting live information about cryptocurrencies

## __Python, SQLAlchemy and Coingecko__  

In this project I worked with Python, SQLAlchemy and Coingecko API to develop a simple Cli console to manage investments and portfolios of clients.
First of all I installed SQLAlchemy to work with a SQLLite database locally:

`pip install sqlalchemy`

Then I got into Coingecko website and explore the endpoints until I got the public API to get the info. 
Then I created a function to get the information of the coins and currencies:


```
import requests

def get_coin_prices(coins, currencies):

    coin = ",".join(coins)
    currency = ",".join(currencies)
    COINGECKO_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"

    data = requests.get(COINGECKO_URL).json()

   return data
```

This function returns the price info that is shown in Coingecko website:
![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/e84d717b-510a-4891-9a20-b7cb900fb4a8)

After that I proceeded to create 2 main classes, Portfolio and Investment. The portfolio class will create instances of portfolios that will host investments. Each investment has a relationship with 1 portfolio, and it can't exists if there is no portfolio.

The basic strcture with SQLAlchemy approach is something like:

```
from typing import List
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base

class Portfolio(Base):
    __tablename__ = "portfolio"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    investments: Mapped[List["Investment"]] = relationship(back_populates="portfolio")

    def __repr__(self) -> str:
        return f"<Portfolio name: {self.name}>"
```

```
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base

class Investment(Base):
    __tablename__ = "investment"

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5,2))

    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id"))
    portfolio: Mapped["Portfolio"] = relationship(back_populates="investments")

    def __repr__(self) -> str:
        return f"Investment coin: {self.coin}, currency: {self.currency} amount: {self.amount}"
```

In both tables I defined the FK, the Portfolio class has a list of investments, which is an easy way to store a collection of investments for each portfolio.

Then in Investment class I mapped the id of portfolio, to indicate that all investments must have a portfolio.

After that I created 4 commands, each one belong to a class with their implementation:
 - Create a portfolio
 - Create an investment
 - View a portfolio
 - Clear the database

Then I setted up in the main the commands to work with the command line:

```
@click.group()
def cli():
    pass

cli.add_command(clear_database)
cli.add_command(add_portfolio)
cli.add_command(add_investment)
cli.add_command(view_portfolio)
```
## Demo

If I execute the program without any commands, it shows the features it has like it was supoosed to do:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/7761fe48-10b7-4183-a712-aba9cd485089)

Then I created my own portfolio:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/29ce0cc2-b1f5-41fd-bc43-7c9346527baa)

And if I try to see if everything went ok, I can check the database through the IDE's extension for SQLite:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/56394572-3198-4ea9-a186-4610fb5849ed)

Then I created an investment for the portfolio previously created:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/cf5b6e00-650e-4b5b-a8bc-9ba2d1165275)

Everything went ok in the investment table too:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/75d617b8-a39e-41ae-a1c5-3aaaf646872d)


I added it one more investment, one ethereum, then I checked through Cli the information:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/c8347bd5-a7f0-44bc-9406-2388cf2f094a)

And if I go to the website to see the prices:

![image](https://github.com/emilianoregazzoni/manager_investments/assets/20979227/38f80d1b-4127-4e0b-bde0-c635c44b93ca)

I can see the information is traveling perfect through the API from Coingecko.

There are minimal price differences, because free APIs can sometimes have a slight delay in updating prices compared to the real-time information displayed on the website.



