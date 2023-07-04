from sqlalchemy.orm import Session
from sqlalchemy import update
from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositorioJogo:

    def __init__(self, session: Session):
        self.session = session

    def criar(self, schema_jogo: schemas.JogoCadastro):
        model_jogo = models.Jogo(nome=schema_jogo.nome,
                                 id_plataforma=schema_jogo.id_plataforma,
                                 ano=schema_jogo.ano,
                                 categoria=schema_jogo.categoria,
                                 desenvolvedora=schema_jogo.desenvolvedora,
                                 observacoes=schema_jogo.observacoes,
                                 progresso=schema_jogo.progresso)
        self.session.add(model_jogo)
        self.session.commit()
        self.session.refresh(model_jogo)
        return model_jogo

    def listar(self):
        return self.session.query(models.Jogo).all()

    def obter(self, id_jogo: int):
        return self.session.query(models.Jogo).filter_by(id=id_jogo).first()

    def atualizar(self, id_jogo: int, schema_jogo: schemas.JogoCadastro):
        if not self.obter(id_jogo):
            return None

        update_statement = update(
            models.Jogo).where(
            models.Jogo.id == id_jogo).values(
            nome=schema_jogo.nome,
            ano=schema_jogo.ano,
            categoria=schema_jogo.categoria,
            desenvolvedora=schema_jogo.desenvolvedora,
            observacoes=schema_jogo.observacoes,
            progresso=schema_jogo.progresso)

        self.session.execute(update_statement)
        self.session.commit()
        return self.obter(id_jogo)

    def remover(self, id_jogo: int):
        jogo_a_ser_excluido = self.obter(id_jogo)

        if not jogo_a_ser_excluido:
            return None

        self.session.delete(jogo_a_ser_excluido)
        self.session.commit()
        return {"msg": "removido"}
