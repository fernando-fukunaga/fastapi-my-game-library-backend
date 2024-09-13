# Rotas relacionadas aos jogos:
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.database.config.database import obter_sessao
from src.services import services_jogo
from src.utils.auth_utils import obter_usuario_logado
from src.schemas import schemas

# Criando router para endpoints de jogos, para melhorar o Swagger:
router = APIRouter(tags=["Jogos"])


@router.post("/jogos", response_model=schemas.JogoDadosDetalhados,
             status_code=201)
async def cadastrar_jogo(jogo: schemas.JogoCadastro,
                         usuario_logado=Depends(obter_usuario_logado),
                         session: Session = Depends(obter_sessao)):
    return services_jogo.criar_jogo(session, jogo, usuario_logado)


@router.get("/jogos", response_model=List[schemas.JogoDadosSimples])
async def listar_jogos(usuario_logado=Depends(obter_usuario_logado),
                       session: Session = Depends(obter_sessao)):
    return services_jogo.listar_jogos(session, usuario_logado)


@router.get("/jogos/{id_jogo}", response_model=schemas.JogoDadosDetalhados)
async def obter_jogo(id_jogo: int,
                     usuario_logado=Depends(obter_usuario_logado),
                     session: Session = Depends(obter_sessao)):
    return services_jogo.obter_jogo(session, usuario_logado, id_jogo)


@router.put("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def atualizar_jogo(id_jogo: int,
                         jogo: schemas.JogoPut,
                         usuario_logado=Depends(obter_usuario_logado),
                         session: Session = Depends(obter_sessao)):
    return services_jogo.atualizar_jogo(session, id_jogo, jogo, usuario_logado)


@router.delete("/jogos/{id_jogo}", status_code=204)
async def remover_jogo(id_jogo: int,
                       usuario_logado=Depends(obter_usuario_logado),
                       session: Session = Depends(obter_sessao)):
    return services_jogo.remover_jogo(session, usuario_logado, id_jogo)
