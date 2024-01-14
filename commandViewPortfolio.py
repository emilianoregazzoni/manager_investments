from typing import List

from sqlalchemy import String, Numeric, create_engine, select, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from portfolio import Portfolio
from sqlalchemy import create_engine
from base import Base
import click
from getPrices import get_coin_prices
from engine import engine


engine = create_engine("sqlite:///demo_r.db")
Base.metadata.create_all(engine)

@click.command(help= "View the investments in a portfolio")
def view_portfolio():
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()

        for index, portfolio in enumerate(all_portfolios):
            print(f"{index + 1} : {portfolio.name}")
        
        portfolio_id = int(input("Select a portfolio: ")) - 1
        portfolio = all_portfolios[portfolio_id]

        investments = portfolio.investments

        coins = set(investment.coin for investment in investments)
        currencies = set(investment.currency for investment in investments)


        coin_prices = get_coin_prices(coins, currencies)

        print(f"Investments in {portfolio.name}")
        for index, investment in enumerate(investments):
            coin_price = coin_prices[investment.coin][investment.currency.lower()]
            total_price = float(investment.amount) * coin_price

            print(f"{index +1}: {investment.coin} {total_price:.2f} {investment.currency}")
        print("\nNote: the prices are provided by site Coingecko")