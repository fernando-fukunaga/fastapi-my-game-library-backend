# Rotas relacionadas aos jogos:
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import obter_sessao
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo
from src.utils.auth_utils import obter_usuario_logado
from src.schemas import schemas

# Criando router para endpoints de jogos, para melhorar o Swagger:
router = APIRouter(tags=["Jogos"])


@router.post("/jogos", response_model=schemas.JogoDadosDetalhados,
             status_code=201)
async def cadastrar_jogo(jogo: schemas.JogoCadastro,
                         usuario_logado=Depends(obter_usuario_logado),
                         session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).criar(jogo, usuario_logado)


@router.get("/jogos", response_model=List[schemas.JogoDadosSimples])
async def listar_jogos(usuario_logado=Depends(obter_usuario_logado),
                       session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).listar(usuario_logado)


@router.get("/jogos/{id_jogo}", response_model=schemas.JogoDadosDetalhados)
async def obter_jogo(id_jogo: int,
                     usuario_logado=Depends(obter_usuario_logado),
                     session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).obter(id_jogo, usuario_logado)


@router.put("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def atualizar_jogo(id_jogo: int,
                         jogo: schemas.JogoPut,
                         usuario_logado=Depends(obter_usuario_logado),
                         session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).atualizar(id_jogo, jogo, usuario_logado)


@router.delete("/jogos/{id_jogo}")
async def remover_jogo(id_jogo: int,
                       usuario_logado=Depends(obter_usuario_logado),
                       session: Session = Depends(obter_sessao)):
    return RepositorioJogo(session).remover(id_jogo, usuario_logado)
