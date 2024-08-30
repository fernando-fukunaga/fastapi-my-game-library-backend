# Módulo para interações com a tabela de jogos do banco
from sqlalchemy.orm import Session
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
        str(usuario_logado.id))

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
        jogos = RepositorioJogo(session).select_jogos("id_plataforma",
                                                      str(plataforma.id))
        if jogos:
            lista_de_jogos.extend(jogos)
    
    return lista_de_jogos


def obter_jogo(session: Session,
               usuario_logado: models.Usuario,
               id_jogo: int) -> models.Jogo:
    jogo = RepositorioJogo(session).select_jogo("id", str(id_jogo))

    if not jogo:
        raise errors.erro_404("Jogo não encontrado!")

    lista_de_plataformas_usuario = RepositorioPlataforma(session).select_plataformas(
        "id_usuario", str(usuario_logado.id)
    )

    for plataforma in lista_de_plataformas_usuario:
        if plataforma.id != jogo.id_plataforma:
            raise errors.erro_404("Jogo não encontrado!")

    return jogo


def atualizar_jogo(session: Session,
                   id_jogo: int,
                   novo_jogo: schemas.JogoPut,
                   usuario_logado: models.Usuario) -> models.Jogo:
    lista_de_jogos_usuario = listar_jogos(session, usuario_logado)

    if not lista_de_jogos_usuario:
        raise errors.erro_404("Jogo não encontrado!")

    for jogo in lista_de_jogos_usuario:
        if jogo.id == id_jogo:
            return RepositorioJogo(session).update_jogo(id_jogo,
                                                        novo_jogo)

    raise errors.erro_404("Jogo não encontrado!")


def remover_jogo(session: Session,
                 usuario_logado: models.Usuario,
                 id_jogo: int) -> None:
    lista_de_jogos_usuario = listar_jogos(session, usuario_logado)

    if not lista_de_jogos_usuario:
        raise errors.erro_404("Jogo não encontrado!")

    for jogo in lista_de_jogos_usuario:
        if jogo.id == id_jogo:
            return RepositorioJogo(session).delete_jogo(jogo)

    raise errors.erro_404("Jogo não encontrado!")
