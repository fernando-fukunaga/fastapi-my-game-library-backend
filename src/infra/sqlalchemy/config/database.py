from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:senha@localhost:3306/my-game-library"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_banco_de_dados():
    Base.metadata.create_all(bind=engine)

def get_banco_de_dados():
    banco_de_dados = SessionLocal()
    try:
        yield banco_de_dados
    finally:
        banco_de_dados.close()