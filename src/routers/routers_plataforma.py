from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import obter_sessao
from src.schemas import schemas
from src.utils.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import \
    RepositorioPlataforma

router = APIRouter(tags=["Plataformas"])


@router.post("/plataformas", response_model=schemas.PlataformaDadosSimples,
             status_code=201)
async def cadastrar_plataforma(plataforma: schemas.PlataformaCadastro,
                               usuario_logado=Depends(obter_usuario_logado),
                               session: Session = Depends(obter_sessao)):
    return RepositorioPlataforma(session).criar(plataforma, usuario_logado)


@router.get("/plataformas",
            response_model=List[schemas.PlataformaDadosSimples],)
async def listar_plataformas(usuario_logado=Depends(obter_usuario_logado),
                             session: Session = Depends(obter_sessao)):
    return RepositorioPlataforma(session).listar(usuario_logado)


@router.get("/plataformas/{id_plataforma}",
            response_model=schemas.PlataformaDadosDetalhados)
async def obter_plataforma(id_plataforma: int,
                           usuario_logado=Depends(obter_usuario_logado),
                           session: Session = Depends(obter_sessao)):
    return RepositorioPlataforma(session).obter(id_plataforma,
                                                usuario_logado)


@router.put("/plataformas/{id_plataforma}",
            response_model=schemas.PlataformaDadosSimples)
async def atualizar_plataforma(id_plataforma: int,
                               plataforma: schemas.PlataformaCadastro,
                               usuario_logado=Depends(obter_usuario_logado),
                               session: Session = Depends(obter_sessao)):
    return RepositorioPlataforma(session).atualizar(id_plataforma, plataforma,
                                                    usuario_logado)


@router.delete("/plataformas/{id_plataforma}")
async def remover_plataforma(id_plataforma: int,
                             usuario_logado=Depends(obter_usuario_logado),
                             session: Session = Depends(obter_sessao)):
    return RepositorioPlataforma(session).remover(id_plataforma,
                                                  usuario_logado)
