# Configuration de SQLAlchemy (engine, session, base)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///db.sqlite3")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
