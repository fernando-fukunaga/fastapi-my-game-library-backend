from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas

class RepositorioJogo:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar(self, schema_jogo: schemas.Jogo):
        model_jogo = models.Jogo(nome=schema_jogo.nome,
                                 id_plataforma=schema_jogo.id_plataforma,
                                 ano=schema_jogo.ano,
                                 categoria=schema_jogo.categoria,
                                 desenvolvedora=schema_jogo.desenvolvedora,
                                 id_usuario=schema_jogo.id_usuario,
                                 observacoes=schema_jogo.observacoes,
                                 status=schema_jogo.status)
        self.banco_de_dados.add(model_jogo)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_jogo)
        return model_jogo

    def listar(self):
        lista_jogos = self.banco_de_dados.query(models.Jogo).all()
        return lista_jogos