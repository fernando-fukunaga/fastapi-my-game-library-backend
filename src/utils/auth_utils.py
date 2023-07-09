from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.providers.token_provider import verificar_token
from src.infra.sqlalchemy.repositorios.repositorio_usuario import \
    RepositorioUsuario
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def obter_usuario_logado(token: str = Depends(oauth2_schema),
                         session: Session = Depends(obter_sessao)):
    try:
        username = verificar_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido!")

    if not username:
        raise HTTPException(status_code=401, detail="Token inválido!")

    usuario = RepositorioUsuario(session).obter_por_username(username)

    if not usuario:
        raise HTTPException(status_code=401, detail="Token inválido!")

    return usuario
