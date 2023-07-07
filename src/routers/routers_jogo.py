from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo
from src.schemas import schemas

router = APIRouter(tags=["Jogos"])


@router.post("/jogos", response_model=schemas.JogoDadosSimples,
             status_code=201)
async def cadastrar_jogo(jogo: schemas.JogoCadastro,
                         session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).criar(jogo)


@router.get("/jogos", response_model=List[schemas.JogoDadosSemLista])
async def listar_jogos(session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).listar()


@router.get("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def obter_jogo(id_jogo: int, session: Session = Depends(obter_sessao)):
    jogo = RepositorioJogo(session).obter(id_jogo)

    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado!")

    return jogo


@router.put("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def atualizar_jogo(id_jogo: int,
                         jogo: schemas.JogoPut,
                         session: Session = Depends(obter_sessao)):
    jogo_a_atualizar = RepositorioJogo(session).atualizar(id_jogo, jogo)

    if not jogo_a_atualizar:
        raise HTTPException(status_code=404, detail="Jogo não encontrado!")

    return jogo_a_atualizar


@router.delete("/jogos/{id_jogo}")
async def remover_jogo(id_jogo: int, session: Session = Depends(obter_sessao)):
    jogo = RepositorioJogo(session).remover(id_jogo)

    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado!")

    return jogo
