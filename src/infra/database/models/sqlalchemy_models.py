from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.config.database import Base


class UserSQLAlchemyModel(Base):
    __tablename__ = "users"

    id = Column(String(36), unique=True)
    name = Column(String(55))
    email = Column(String(45), unique=True)
    username = Column(String(14), unique=True)
    password = Column(String(100))

    platforms = relationship("PlatformSQLALchemyModel", back_populates="users")


class Plataforma(Base):
    __tablename__ = "plataforma"

    id = Column(Integer, primary_key=True)
    nome = Column(String(55))
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    fabricante = Column(String(15))
    observacoes = Column(String(100))

    usuario = relationship("Usuario", back_populates="plataformas")
    jogos = relationship("Jogo", back_populates="plataforma")


class Jogo(Base):
    __tablename__ = "jogo"

    id = Column(Integer, primary_key=True)
    nome = Column(String(55))
    id_plataforma = Column(Integer, ForeignKey("plataforma.id"))
    ano = Column(Integer)
    categoria = Column(String(20))
    desenvolvedora = Column(String(15))
    observacoes = Column(String(100))
    progresso = Column(DECIMAL(3, 2))

    plataforma = relationship("Plataforma", back_populates="jogos")
