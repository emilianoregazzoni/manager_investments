import click
from sqlalchemy import create_engine
from base import Base
from commandViewPortfolio import view_portfolio
from commandClearDatabase import clear_database
from commandCreatePortfolio import add_portfolio
from commandCreateInvestment import add_investment

engine = create_engine("sqlite:///demo_r.db")
Base.metadata.create_all(engine)

@click.group()
def cli():
    pass

cli.add_command(clear_database)
cli.add_command(add_portfolio)
cli.add_command(add_investment)
cli.add_command(view_portfolio)

if __name__ == '__main__':
    cli()