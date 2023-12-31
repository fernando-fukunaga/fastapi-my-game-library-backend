# Módulo para interações com a tabela de plataformas do banco
from sqlalchemy.orm import Session
from sqlalchemy import update, and_
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.errors import errors


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

    def criar(self, schema_plataforma: schemas.PlataformaCadastro,
              usuario_logado: models.Usuario):
        model_plataforma = models.Plataforma(
            nome=schema_plataforma.nome,
            id_usuario=usuario_logado.id,
            fabricante=schema_plataforma.fabricante,
            observacoes=schema_plataforma.observacoes)
        self.session.add(model_plataforma)
        self.session.commit()
        self.session.refresh(model_plataforma)
        return model_plataforma

    def listar(self, usuario_logado: models.Usuario):
        return (self.session.query(models.Plataforma).
                filter_by(id_usuario=usuario_logado.id).
                all())

    def obter(self, id_plataforma: int, usuario_logado: models.Usuario):
        plataforma_encontrada = (self.session.query(models.Plataforma).
                                 filter_by(id=id_plataforma,
                                           id_usuario=usuario_logado.id).
                                 first())

        if not plataforma_encontrada:
            raise errors.erro_404("Plataforma não encontrada!")

        return plataforma_encontrada

    def atualizar(self, id_plataforma: int,
                  schema_plataforma: schemas.PlataformaCadastro,
                  usuario_logado: models.Usuario):
        try:
            self.obter(id_plataforma, usuario_logado)
        except:
            raise errors.erro_404("Plataforma não encontrada!")

        update_statement = (update(models.Plataforma).
                            where(and_(models.Plataforma.id == id_plataforma,
                                       models.Plataforma.id_usuario ==
                                       usuario_logado.id)).
                            values(nome=schema_plataforma.nome,
                                   fabricante=schema_plataforma.fabricante,
                                   observacoes=schema_plataforma.observacoes))

        self.session.execute(update_statement)
        self.session.commit()
        return self.obter(id_plataforma, usuario_logado)

    def remover(self, id_plataforma: int, usuario_logado: models.Usuario):
        plataforma_a_ser_excluida = self.obter(id_plataforma, usuario_logado)

        if not plataforma_a_ser_excluida:
            raise errors.erro_404("Plataforma não encontrada!")

        self.session.delete(plataforma_a_ser_excluida)
        self.session.commit()
        return {"msg": "removido"}
