# Módulo para interações com a tabela de jogos do banco
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import RepositorioPlataforma
from src.schemas import schemas
from src.errors import errors
from typing import List


def _usuario_possui_plataforma(session: Session,
                               jogo: models.Jogo,
                               usuario_logado: models.Usuario) -> bool:
    plataformas = RepositorioPlataforma(session).select_plataformas(
        "id_usuario",
        usuario_logado.id)

    if not plataformas:
        return False
    
    for plataforma in plataformas:
        if plataforma.id == jogo.id_plataforma:
            return True

    return False


def criar_jogo(session: Session,
               payload: schemas.JogoCadastro,
               usuario_logado: models.Usuario):
    jogo = models.Jogo(nome=payload.nome,
                       id_plataforma=payload.id_plataforma,
                       ano=payload.ano,
                       categoria=payload.categoria,
                       desenvolvedora=payload.desenvolvedora,
                       observacoes=payload.observacoes,
                       progresso=payload.progresso)

    if not _usuario_possui_plataforma(session, jogo, usuario_logado):
        raise errors.erro_400("Usuário não possui essa plataforma!")

    return RepositorioJogo(session).insert_jogo(jogo)


def listar_jogos(session: Session,
                 usuario_logado: models.Usuario) -> List[models.Jogo]:
    lista_de_plataformas = RepositorioPlataforma(session).select_plataformas(
        "id_usuario", str(usuario_logado.id)
    )

    if not lista_de_plataformas:
        return []

    lista_de_jogos = []
    for plataforma in lista_de_plataformas:
        lista_de_jogos.extend(
            RepositorioJogo(session).select_jogos("id_plataforma",
                                                  str(plataforma.id))
        )
    
    return lista_de_jogos
