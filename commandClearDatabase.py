from base import Base
from engine import engine
import click

@click.command(help= "Drop all tables")
def clear_database():
    Base.metadata.drop_all(engine)
    print("Database cleared :)")