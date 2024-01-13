from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from portfolio import Portfolio

import click
from engine import engine

@click.command(help= "Create a new portfolio")
@click.option("--name", prompt=True)
@click.option("--description", prompt=True)
def add_portfolio(name, description):
    portfolio = Portfolio(name = name, description = description)
    with Session(engine) as session:
        session.add(portfolio)
        session.commit()
    print(f"Portolio {name} created OK!")