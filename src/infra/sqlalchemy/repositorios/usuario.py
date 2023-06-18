from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario:

    def __init__(self, banco_de_dados: Session):
        self.banco_de_dados = banco_de_dados

    def criar(self, schema_usuario: schemas.Usuario):
        model_usuario = models.Usuario(nome=schema_usuario.nome,
                                       email=schema_usuario.email,
                                       username=schema_usuario.username,
                                       senha=schema_usuario.senha)
        self.banco_de_dados.add(model_usuario)
        self.banco_de_dados.commit()
        self.banco_de_dados.refresh(model_usuario)
        return model_usuario
    
    def listar(self):
        lista_usuarios = self.banco_de_dados.query(models.Usuario).all()
        return lista_usuarios