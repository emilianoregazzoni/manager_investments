from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from portfolio import Portfolio

import click
from engine import engine
from investment import Investment

@click.group()
def cli():
    pass

@click.command(help= "Create an investment and add it to a portfolio")
@click.option("--coin", prompt=True)
@click.option("--currency", prompt=True)
@click.option("--amount", prompt=True)
def add_investment(coin, currency, amount):
    with Session(engine) as session:
        stmt = select(Portfolio)
        all_portfolios = session.execute(stmt).scalars().all()
        for index, portfolio in enumerate(all_portfolios):
            print(f"{index + 1} : {portfolio.name}")

        portfolio_index = int(input("Select a porfolio: ")) - 1
        portfolio = all_portfolios[portfolio_index]

        investment = Investment(coin=coin, currency=currency, amount=amount)
        portfolio.investments.append(investment)

        session.add(portfolio)
        session.commit()
            
        print(f"Added new{coin} investment to {portfolio.name}")