from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario:

    def __init__(self, session: Session):
        self.session = session

    def criar(self, schema_usuario: schemas.UsuarioCadastro):
        model_usuario = models.Usuario(nome=schema_usuario.nome,
                                       email=schema_usuario.email,
                                       username=schema_usuario.username,
                                       senha=schema_usuario.senha)
        self.session.add(model_usuario)
        self.session.commit()
        self.session.refresh(model_usuario)
        return model_usuario
    
    def listar(self):
        return self.session.query(models.Usuario).all()
    
    def obter(self, id_usuario: int):
        return self.session.query(models.Usuario).filter_by(id=id_usuario).first()
    
    def remover(self, id_usuario: int):
        usuario_a_ser_excluido = self.obter(id_usuario)
        self.session.delete(usuario_a_ser_excluido)
        self.session.commit()
        return {"msg":"removido"}