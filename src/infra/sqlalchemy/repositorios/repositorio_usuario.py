from sqlalchemy.orm import Session
from sqlalchemy import update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.providers.hash_provider import gerar_hash, verificar_senha
from src.infra.providers.token_provider import gerar_token
from src.errors import errors


class RepositorioUsuario:

    def __init__(self, session: Session):
        self.session = session

    def verifica_email_ja_cadastrado(self, email: str) -> bool:
        if self.session.query(models.Usuario).filter_by(email=email).first():
            return True
        return False

    def verifica_username_ja_cadastrado(self, username: str) -> bool:
        if self.session.query(models.
                              Usuario).filter_by(username=username).first():
            return True
        return False

    def verifica_username_muito_grande(self, username: str) -> bool:
        if len(username) > 14:
            return True
        return False

    def criar(self, schema_usuario: schemas.UsuarioCadastro):
        if self.verifica_email_ja_cadastrado(schema_usuario.email):
            raise errors.erro_400_email_ja_cadastrado

        if self.verifica_username_ja_cadastrado(schema_usuario.username):
            raise errors.erro_400_username_ja_cadastrado

        if self.verifica_username_muito_grande(schema_usuario.username):
            raise errors.erro_400_username_muito_grande

        model_usuario = models.Usuario(nome=schema_usuario.nome,
                                       email=schema_usuario.email,
                                       username=schema_usuario.username,
                                       senha=gerar_hash(schema_usuario.senha))

        self.session.add(model_usuario)
        self.session.commit()
        self.session.refresh(model_usuario)
        return model_usuario

    def obter_por_username(self, username: str):
        return self.session.query(
            models.Usuario).filter_by(username=username).first()

    def autenticar(self, username: str, senha: str):
        model_usuario = self.obter_por_username(username)

        if not model_usuario:
            raise errors.erro_400_login_incorreto

        if not verificar_senha(senha, model_usuario.senha):
            raise errors.erro_400_login_incorreto

        token = gerar_token({"username": username})

        return schemas.Token(usuario=model_usuario, access_token=token)
