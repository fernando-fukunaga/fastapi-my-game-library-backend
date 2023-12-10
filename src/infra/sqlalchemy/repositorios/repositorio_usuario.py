# Módulo para interações com a tabela de usuarios do banco
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.models import models
from src.errors import errors


class RepositorioUsuario:
    """Classe de interações com o banco de dados.

    Exemplo de instânciação:

    repositorio = RepositorioUsuario(session)

    Attributes:
        session (Session): sessão do SQLAlchemy para escrita e leitura
        no nosso banco.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_usuario(self, usuario: models.Usuario) -> models.Usuario:
        try:
            self.session.add(usuario)
            self.session.commit()
        except Exception as e:
            print(e)
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

        return usuario

    def select_usuario(self, column: str, value: str) -> models.Usuario:
        try:
            usuario = self.session.query(
                models.Usuario).filter_by(**{column:value}).first()
        except Exception as e:
            print(e)
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
        
        if not usuario:
            return None
        
        return usuario
