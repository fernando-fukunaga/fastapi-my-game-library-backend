from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.sqlalchemy.repositorios.repositorio_usuario import \
    RepositorioUsuario
from src.infra.sqlalchemy.models import models
from src.infra.providers.token_provider import gerar_token
from src.utils.auth_utils import obter_usuario_logado

router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/signup", response_model=schemas.UsuarioDadosSimples,
             status_code=201)
async def cadastar_usuario(usuario: schemas.UsuarioCadastro,
                           session: Session = Depends(obter_sessao)):
    return RepositorioUsuario(session).criar(usuario)


@router.post("/login", response_model=schemas.Token)
async def login(form_data=Depends(OAuth2PasswordRequestForm),
                session: Session = Depends(obter_sessao)):
    username = form_data.username
    senha = form_data.password

    credenciais_corretas = RepositorioUsuario(session).autenticar(username,
                                                                  senha)

    if not credenciais_corretas:
        raise HTTPException(status_code=400,
                            detail="Usuário ou senha incorretos!")

    token = gerar_token({"username": username})

    return schemas.Token(usuario=credenciais_corretas,
                         access_token=token)


@router.get("/me", response_model=schemas.UsuarioDadosSemLista)
async def me(usuario: models.Usuario = Depends(obter_usuario_logado)):
    return usuario
