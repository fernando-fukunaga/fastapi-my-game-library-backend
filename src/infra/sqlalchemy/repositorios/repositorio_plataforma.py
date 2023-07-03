from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPlataforma:

    def __init__(self, session: Session):
        self.session = session

    def criar(self, schema_plataforma: schemas.PlataformaCadastro):
        model_plataforma = models.Plataforma(nome=schema_plataforma.nome,                                            
                                             id_usuario=schema_plataforma.id_usuario,
                                             fabricante=schema_plataforma.fabricante,
                                             observacoes=schema_plataforma.observacoes)                                          
        self.session.add(model_plataforma)
        self.session.commit()
        self.session.refresh(model_plataforma)
        return model_plataforma

    def listar(self):
        return self.session.query(models.Plataforma).all()
    
    def obter(self, id_plataforma: int):
        return self.session.query(models.Plataforma).filter_by(id=id_plataforma).first()
    
    def remover(self, id_plataforma: int):
        plataforma_a_ser_excluida = self.obter(id_plataforma)
        self.session.delete(plataforma_a_ser_excluida)
        self.session.commit()
        return {"msg":"removido"}