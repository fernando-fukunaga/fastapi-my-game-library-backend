# Rotas relacionadas à autenticação e autorização:
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.sqlalchemy.repositorios.repositorio_usuario import \
    RepositorioUsuario
from src.infra.sqlalchemy.models import models
from src.utils.auth_utils import obter_usuario_logado

"""Criando router para endpoints de autenticação,
para melhorar o Swagger, com prefixo /auth:"""
router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post("/signup", response_model=schemas.UsuarioDadosSimples,
             status_code=201)
async def cadastrar_usuario(usuario: schemas.UsuarioCadastro,
                            session: Session = Depends(obter_sessao)):
    return RepositorioUsuario(session).criar(usuario)


@router.post("/login")
async def login(form_data=Depends(OAuth2PasswordRequestForm),
                session: Session = Depends(obter_sessao)):
    username = form_data.username
    senha = form_data.password

    return RepositorioUsuario(session).autenticar(username, senha)


@router.get("/me", response_model=schemas.UsuarioDadosSimples)
async def me(usuario: models.Usuario = Depends(obter_usuario_logado)):
    return usuario
