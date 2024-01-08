# Rotas relacionadas às plataformas:
from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import obter_sessao
from src.schemas import schemas
from src.utils.auth_utils import obter_usuario_logado
from src.services import services_plataforma

# Criando router para endpoints de plataformas, para melhorar o Swagger:
router = APIRouter(tags=["Plataformas"])


@router.post("/plataformas", response_model=schemas.PlataformaDadosSimples,
             status_code=201)
async def cadastrar_plataforma(plataforma: schemas.PlataformaCadastro,
                               usuario_logado=Depends(obter_usuario_logado),
                               session: Session = Depends(obter_sessao)):
    return services_plataforma.criar_plataforma(session,
                                                plataforma,
                                                usuario_logado)


@router.get("/plataformas",
            response_model=List[schemas.PlataformaDadosSimples],)
async def listar_plataformas(usuario_logado=Depends(obter_usuario_logado),
                             session: Session = Depends(obter_sessao)):
    return services_plataforma.listar_plataformas(session,
                                                  usuario_logado)


@router.get("/plataformas/{id_plataforma}",
            response_model=schemas.PlataformaDadosDetalhados)
async def obter_plataforma(id_plataforma: int,
                           usuario_logado=Depends(obter_usuario_logado),
                           session: Session = Depends(obter_sessao)):
    return services_plataforma.obter_plataforma(session,
                                                id_plataforma,
                                                usuario_logado)


@router.put("/plataformas/{id_plataforma}",
            response_model=schemas.PlataformaDadosSimples)
async def atualizar_plataforma(id_plataforma: int,
                               plataforma: schemas.PlataformaCadastro,
                               usuario_logado=Depends(obter_usuario_logado),
                               session: Session = Depends(obter_sessao)):
    return services_plataforma.atualizar_plataforma(session,
                                                    id_plataforma,
                                                    plataforma,
                                                    usuario_logado)


@router.delete("/plataformas/{id_plataforma}")
async def remover_plataforma(id_plataforma: int,
                             usuario_logado=Depends(obter_usuario_logado),
                             session: Session = Depends(obter_sessao)):
    return services_plataforma.remover_plataforma(session,
                                                  id_plataforma,
                                                  usuario_logado)
