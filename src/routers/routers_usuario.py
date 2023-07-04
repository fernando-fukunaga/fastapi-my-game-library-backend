from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

router = APIRouter()


@router.post("/usuarios", response_model=schemas.UsuarioDadosSimples,
             status_code=201)
async def cadastar_usuario(usuario: schemas.UsuarioCadastro,
                           session: Session = Depends(obter_sessao)):
    return RepositorioUsuario(session).criar(usuario)


@router.get("/usuarios", response_model=List[schemas.UsuarioDadosSemLista])
async def listar_usuarios(session: Session = Depends(obter_sessao)):
    return RepositorioUsuario(session).listar()


@router.get("/usuarios/{id_usuario}",
            response_model=schemas.UsuarioDadosSimples)
async def obter_usuario(id_usuario: int,
                        session: Session = Depends(obter_sessao)):
    usuario = RepositorioUsuario(session).obter(id_usuario)

    if not usuario:
        raise HTTPException(
            status_code=404, detail="Usuário não encontrado!")

    return usuario


@router.put("/usuarios/{id_usuario}",
            response_model=schemas.UsuarioDadosSimples)
async def atualizar_usuario(id_usuario: int, usuario: schemas.UsuarioCadastro,
                            session: Session = Depends(obter_sessao)):
    usuario_a_atualizar = RepositorioUsuario(session).atualizar(
        id_usuario, usuario)

    if not usuario_a_atualizar:
        raise HTTPException(status_code=404, detail="Usuario não encontrado!")

    return usuario_a_atualizar


@router.delete("/usuarios/{id_usuario}")
async def remover_usuario(id_usuario: int,
                          session: Session = Depends(obter_sessao)):
    usuario = RepositorioUsuario(session).remover(id_usuario)

    if not usuario:
        raise HTTPException(
            status_code=404, detail="Usuário não encontrado!")

    return usuario
