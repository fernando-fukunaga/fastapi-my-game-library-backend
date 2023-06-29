from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas_jogo

class RepositorioJogo:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar(self, schema_jogo: schemas_jogo.JogoCadastro):
        model_jogo = models.Jogo(nome=schema_jogo.nome,
                                 id_plataforma=schema_jogo.id_plataforma,
                                 ano=schema_jogo.ano,
                                 categoria=schema_jogo.categoria,
                                 desenvolvedora=schema_jogo.desenvolvedora,
                                 id_usuario=schema_jogo.id_usuario,
                                 observacoes=schema_jogo.observacoes,
                                 progresso=schema_jogo.progresso)
        self.banco_de_dados.add(model_jogo)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_jogo)
        return model_jogo

    def listar(self):
        return self.banco_de_dados.query(models.Jogo).all()
    
    def obter(self, id_jogo: int):
        return self.banco_de_dados.query(models.Jogo).filter_by(id=id_jogo).first()
    
    def remover(self, id_jogo: int):
        jogo_a_ser_excluido = self.obter(id_jogo)
        self.banco_de_dados.delete(jogo_a_ser_excluido)
        self.banco_de_dados.commit()
        return {"msg":"removido"}