from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from jose import JWTError
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.providers.token_provider import verificar_token
from src.errors import errors
from src.infra.sqlalchemy.repositorios.repositorio_usuario import \
    RepositorioUsuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def obter_usuario_logado(token: str = Depends(oauth2_schema),
                         session: Session = Depends(obter_sessao)):
    try:
        username = verificar_token(token)
    except JWTError:
        raise errors.erro_401_token_invalido

    if not username:
        raise errors.erro_401_token_invalido

    usuario = RepositorioUsuario(session).obter_por_username(username)

    if not usuario:
        raise errors.erro_401_token_invalido

    return usuario
