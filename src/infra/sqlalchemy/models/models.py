from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    username = Column(String)
    senha = Column(String)