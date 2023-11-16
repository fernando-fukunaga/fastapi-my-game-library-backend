# Módulo para interações com a tabela de usuarios do banco
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.providers.hash_provider import gerar_hash, verificar_senha
from src.infra.providers.token_provider import gerar_token
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
        self.session.add(usuario)
        self.session.commit()
        return usuario

    def select_usuarios():
        pass