# Helpers envolvendo sistema de autenticação e segurança
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from jose import JWTError
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.providers.token_provider import verificar_token
from src.errors import errors
from src.infra.sqlalchemy.repositorios.repositorio_usuario import \
    RepositorioUsuario

"""Definindo schema de oauth2, para sempre exigir o token nos headers
dos endpoints protegidos:"""
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def obter_usuario_logado(token: str = Depends(oauth2_schema),
                         session: Session = Depends(obter_sessao)):
    """Tentar obter o usuario logado a partir do token passado no header
    da requisição

    Args:
        token (str): JWT passado pelo usuário nos headers
        session (Session): sessão do ORM para conversar com o banco.

    Returns:
        Um objeto de models.Usuario, caso o token esteja correto.

    Raises:
        erro_401: caso o token informado seja inválido.
    """
    try:
        username = verificar_token(token)
    except JWTError:
        raise errors.erro_401("Token inválido ou vencido!")

    if not username:
        raise errors.erro_401("Token inválido ou vencido!")

    usuario = RepositorioUsuario(session).obter_por_username(username)

    if not usuario:
        raise errors.erro_401("Token inválido ou vencido!")

    return usuario
