from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_sessao
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo
from src.schemas import schemas

router = APIRouter()


@router.post("/jogos", response_model=schemas.JogoDadosSimples, status_code=201)
async def cadastrar_jogo(jogo: schemas.JogoCadastro,
                         session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).criar(jogo)


@router.get("/jogos", response_model=List[schemas.JogoDadosSemLista])
async def listar_jogos(session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).listar()


@router.get("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def obter_jogo(id_jogo: int, session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).obter(id_jogo)


@router.put("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def atualizar_jogo(id_jogo: int,
                         jogo: schemas.JogoPut,
                         session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).atualizar(id_jogo, jogo)


@router.delete("/jogos/{id_jogo}")
async def remover_jogo(id_jogo: int, session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).remover(id_jogo)
