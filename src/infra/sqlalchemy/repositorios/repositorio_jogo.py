# Módulo para interações com a tabela de jogos do banco
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.infra.sqlalchemy.models import models
from src.errors import errors
from typing import List
from src.schemas.schemas import JogoPut


class RepositorioJogo:
    """Classe de interações com o banco de dados.

    Exemplo de instânciação:

    repositorio = RepositorioJogo(session)

    Attributes:
        session (Session): sessão do SQLAlchemy para escrita e leitura
        no nosso banco.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_jogo(self, jogo: models.Jogo) -> models.Jogo:
        try:
            self.session.add(jogo)
            self.session.commit()
            return jogo
        except Exception:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

    def select_jogo(self, column: str, value: str) -> models.Jogo:
        try:
            jogo = self.session.query(
                models.Jogo).filter_by(**{column: value}).first()
        except Exception as e:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

        if not jogo:
            return None

        return jogo

    def select_jogos(self, column: str, value: str) -> List[models.Jogo]:
        try:
            jogos = self.session.query(
                models.Jogo).filter_by(**{column:value}).all()
        except Exception as e:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
        
        if not jogos:
            return None
        
        return jogos

    def update_jogo(self,
                    id_jogo: int,
                    novo_jogo: JogoPut) -> models.Jogo:
        try:
            update_statement = (update(models.Jogo).
                                where(models.Jogo.id == id_jogo).
                                values(nome=novo_jogo.nome,
                                       ano=novo_jogo.ano,
                                       categoria=novo_jogo.categoria,
                                       desenvolvedora=novo_jogo.desenvolvedora,
                                       observacoes=novo_jogo.observacoes,
                                       progresso=novo_jogo.progresso))
            self.session.execute(update_statement)
            self.session.commit()
            return self.select_jogo(column="id", value=str(id_jogo))

        except Exception:
            raise errors.erro_500("Ocorreu um erro interno, tente novamente!")

    def delete_jogo(self,
                    jogo: models.Jogo) -> None:
        try:
            self.session.delete(jogo)
            self.session.commit()
            return None

        except Exception:
            raise errors.erro_500("Ocorreu um erro interno, tente novamente!")
