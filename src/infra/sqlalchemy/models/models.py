from sqlalchemy import Column, Integer, String, ForeignKey
from src.infra.sqlalchemy.config.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    username = Column(String)
    senha = Column(String)

class Plataforma(Base):
    __tablename__ = "plataforma"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    fabricante = Column(String)
    observacoes = Column(String)

class Jogo(Base):
    __tablename__ = "jogo"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    id_plataforma = Column(Integer, ForeignKey("plataforma.id"))
    ano = Column(Integer)
    categoria = Column(String)
    desenvolvedora = Column(String)
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    observacoes = Column(String)
    status = Column(String)