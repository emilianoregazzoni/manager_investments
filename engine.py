from sqlalchemy import create_engine
from base import Base

engine = create_engine("sqlite:///demo_r.db")
Base.metadata.create_all(engine)