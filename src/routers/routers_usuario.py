from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import criar_sessao
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

router = APIRouter()


@router.post("/usuarios", response_model=schemas.UsuarioDadosSimples,
             status_code=201)
async def cadastar_usuario(usuario: schemas.UsuarioCadastro,
                           session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).criar(usuario)


@router.get("/usuarios", response_model=List[schemas.UsuarioDadosSemLista])
async def listar_usuarios(session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).listar()


@router.get("/usuarios/{id_usuario}",
            response_model=schemas.UsuarioDadosSimples)
async def obter_usuario(id_usuario: int,
                        session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).obter(id_usuario)


@router.put("/usuarios/{id_usuario}",
            response_model=schemas.UsuarioDadosSimples)
async def atualizar_usuario(id_usuario: int, usuario: schemas.UsuarioCadastro,
                            session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).atualizar(id_usuario, usuario)


@router.delete("/usuarios/{id_usuario}")
async def remover_usuario(id_usuario: int,
                          session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).remover(id_usuario)
