from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.database.config.database import Base


class UserSQLAlchemyModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    email = Column(String(45), unique=True)
    username = Column(String(14), unique=True)
    password = Column(String(100))

    platforms = relationship("Plataforma", back_populates="user")


class Plataforma(Base):
    """Representa a plataforma de algum usuário.

    Será usada pelos repositórios que interagem com o banco.

    Attributes:
        id (int): número de identificação plataforma
        nome (str): nome da plataforma
        id_usuario (int): id do usuário a qual a plataforma pertence
        fabricante (str): nome da empresa que fabrica essa plataforma
        observacoes (str): obervações adicionais
        usuario (UserSQLAlchemyModel): a pessoa dona da plataforma
        jogos (List[Jogo]): lista de jogos desta plataforma
    """
    __tablename__ = "plataforma"

    id = Column(Integer, primary_key=True)
    nome = Column(String(55))
    id_usuario = Column(Integer, ForeignKey("usuario.id"))
    fabricante = Column(String(15))
    observacoes = Column(String(100))

    usuario = relationship("Usuario", back_populates="plataformas")
    jogos = relationship("Jogo", back_populates="plataforma")


class Jogo(Base):
    """Representa os jogos de algum usuário.

    Será usada pelos repositórios que interagem com o banco.

    Attributes:
        id (int): número de identificação jogo
        nome (str): nome djogo
        id_plataforma (int): id da plataforma a qual o jogo pertence
        ano (int): ano de lançamento do jogo
        categoria (str): categoria do jogo
        desenvolvedora (str): nome da desenvolvedora
        observacoes (str): obervações adicionais
        progresso (float): progresso do usuário nesse jogo
        plataforma (Plataforma): plataforma a qual o jogo está atrelado
    """
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
