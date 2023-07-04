from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_sessao
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import RepositorioPlataforma

router = APIRouter()


@router.post("/plataformas", response_model=schemas.PlataformaDadosSimples,
             status_code=201)
async def cadastrar_plataforma(plataforma: schemas.PlataformaCadastro,
                               session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).criar(plataforma)


@router.get("/plataformas",
            response_model=List[schemas.PlataformaDadosSemLista])
async def listar_plataformas(session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).listar()


@router.get("/plataformas/{id_plataforma}",
            response_model=schemas.PlataformaDadosSimples)
async def obter_plataforma(id_plataforma: int,
                           session: Session = Depends(criar_sessao)):
    plataforma = RepositorioPlataforma(session).obter(id_plataforma)

    if not plataforma:
        raise HTTPException(status_code=404, 
                            detail="Plataforma não encontrada!")
    
    return plataforma


@router.put("/plataformas/{id_plataforma}", 
            response_model=schemas.PlataformaDadosSimples)
async def atualizar_plataforma(id_plataforma: int,
                               plataforma: schemas.PlataformaPut,
                               session: Session = Depends(criar_sessao)):
    plataforma_a_atualizar = RepositorioPlataforma(session).atualizar(
        id_plataforma, plataforma)

    if not plataforma_a_atualizar:
        raise HTTPException(status_code=404, 
                            detail="Plataforma não encontrada!")
    
    return plataforma_a_atualizar


@router.delete("/plataformas/{id_plataforma}")
async def remover_plataforma(id_plataforma: int,
                             session: Session = Depends(criar_sessao)):
    plataforma = RepositorioPlataforma(session).remover(id_plataforma)

    if not plataforma:
        raise HTTPException(status_code=404, 
                            detail="Plataforma não encontrada!")
    
    return plataforma
