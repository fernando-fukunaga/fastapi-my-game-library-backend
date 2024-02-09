from sqlalchemy.orm import Session
from src.schemas.schemas import PlataformaCadastro
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import RepositorioPlataforma
from typing import List
from src.errors import errors


def criar_plataforma(session: Session,
                     payload: PlataformaCadastro,
                     usuario_logado: models.Usuario) -> models.Plataforma:
    plataforma = models.Plataforma(id_usuario=usuario_logado.id,
                                   nome=payload.nome,
                                   fabricante=payload.fabricante,
                                   observacoes=payload.observacoes)
    return RepositorioPlataforma(session).insert_plataforma(plataforma)


def listar_plataformas(session: Session,
                       usuario_logado: models.Usuario) -> List[models.
                                                               Plataforma]:
    id_usuario = str(usuario_logado.id)
    return RepositorioPlataforma(session).select_plataformas(
        column="id_usuario", value=id_usuario)


def obter_plataforma(session: Session,
                     id_plataforma: int,
                     usuario_logado: models.Usuario) -> models.Plataforma:
    query_result = RepositorioPlataforma(session).select_plataforma(
        column="id", value=str(id_plataforma))
    if query_result == None:
        raise errors.erro_404("Plataforma não encontrada!")
    elif query_result.id_usuario == usuario_logado.id:
        return query_result
    else:
        raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

def atualizar_plataforma(
        session: Session,
        id_plataforma: int,
        nova_plataforma: PlataformaCadastro,
        usuario_logado: models.Usuario) -> models.Plataforma:
    plataforma_existe = RepositorioPlataforma(session).select_plataforma(
        "id", str(id_plataforma))
    
    if not plataforma_existe:
        raise errors.erro_404("Plataforma não encontrada!")
    
    if plataforma_existe.id_usuario != usuario_logado.id:
        raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
    
    return RepositorioPlataforma(session).update_plataforma(
        id_plataforma,
        nova_plataforma)


def remover_plataforma(
        session: Session,
        id_plataforma: int,
        usuario_logado: models.Usuario) -> dict:
    plataforma_a_ser_excluida = RepositorioPlataforma(
        session).select_plataforma("id", str(id_plataforma))

    if not plataforma_a_ser_excluida:
        raise errors.erro_404("Plataforma não encontrada!")
    
    if plataforma_a_ser_excluida.id_usuario != usuario_logado.id:
        raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
    
    RepositorioPlataforma(session).delete_plataforma(
        plataforma_a_ser_excluida)
    return {}
