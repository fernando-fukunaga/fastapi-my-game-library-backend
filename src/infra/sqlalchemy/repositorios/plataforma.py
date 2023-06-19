from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPlataforma:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar(self, schema_plataforma: schemas.Plataforma):
        model_plataforma = models.Plataforma(nome=schema_plataforma.nome,                                            
                                             id_usuario=schema_plataforma.id_usuario,
                                             fabricante=schema_plataforma.fabricante,
                                             observacoes=schema_plataforma.observacoes)                                          
        self.banco_de_dados.add(model_plataforma)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_plataforma)
        return model_plataforma

    def listar(self):
        return self.banco_de_dados.query(models.Plataforma).all()
    
    def obter(self, id_plataforma: int):
        return self.banco_de_dados.query(models.Plataforma).filter_by(id=id_plataforma).first()
    
    def remover(self, id_plataforma: int):
        plataforma_a_ser_excluida = self.obter(id_plataforma)
        self.banco_de_dados.delete(plataforma_a_ser_excluida)
        self.banco_de_dados.commit()
        return {"msg":"removido"}