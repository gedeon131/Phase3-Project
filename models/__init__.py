from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Connexion SQLite (fichier local database.db)
engine = create_engine("sqlite:///database.db")

# Base ORM
Base = declarative_base()

# Session pour interagir avec la DB
Session = sessionmaker(bind=engine)
session = Session()