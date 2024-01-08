# Módulo para interações com a tabela de plataformas do banco
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas.schemas import PlataformaCadastro
from src.errors import errors
from typing import List
from sqlalchemy import update


class RepositorioPlataforma:
    """Classe de interações com o banco de dados.

    Exemplo de instânciação:

    repositorio = RepositorioPlataforma(session)

    Attributes:
        session (Session): sessão do SQLAlchemy para escrita e leitura
        no nosso banco.
    """
    def __init__(self, session: Session) -> None:
        self.session = session

    def insert_plataforma(self,
                          plataforma: models.Plataforma) -> models.Plataforma:
        try:
            self.session.add(plataforma)
            self.session.commit()
        except Exception as e:
            print(e)
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

        return plataforma

    def select_plataforma(self, column: str, value: str) -> models.Plataforma:
        try:
            plataforma = self.session.query(
                models.Plataforma).filter_by(**{column:value}).first()
        except Exception as e:
            print(e)
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
        
        if not plataforma:
            return None
        
        return plataforma
    
    def select_plataformas(self, column: str, value: str) -> List[models.Plataforma]:
        try:
            plataformas = self.session.query(
                models.Plataforma).filter_by(**{column:value}).all()
        except Exception as e:
            print(e)
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
        
        if not plataformas:
            return None

        return plataformas

    def update_plataforma(
            self,
            id: int,
            nova_plataforma: PlataformaCadastro) -> models.Plataforma:
        try:
            update_statement = (update(models.Plataforma).
                                where(models.Plataforma.id == id).
                                values(
                                    nome=nova_plataforma.nome,
                                    fabricante=nova_plataforma.fabricante,
                                    observacoes=nova_plataforma.observacoes))

            self.session.execute(update_statement)
            self.session.commit()
            return self.select_plataforma("id", str(id))

        except Exception:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")

    def delete_plataforma(self,
                          plataforma: models.Plataforma) -> None:
        try:
            self.session.delete(plataforma)
            self.session.commit()
            return None

        except Exception:
            raise errors.erro_500("Ocorreu um erro interno! Tente novamente!")
