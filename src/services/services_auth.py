from src.infra.database.repositories.impl.sqlalchemy_user_repository import RepositorioUsuario
from src.infra.providers.hash_provider import gerar_hash, verificar_senha
from src.infra.providers.token_provider import gerar_token
from src.schemas import schemas
from src.infra.database.models import sqlalchemy_models
from src.errors import errors
from sqlalchemy.orm import Session


def criar_usuario(session: Session,
                  schema_usuario: schemas.UsuarioCadastro) -> models.UserEntity:
    validar_dados_de_cadastro(session, schema_usuario)

    usuario = models.UserEntity(nome=schema_usuario.nome,
                                email=schema_usuario.email,
                                username=schema_usuario.username,
                                senha=gerar_hash(schema_usuario.senha))
    
    return RepositorioUsuario(session).insert_usuario(usuario)


def autenticar(session: Session, username: str, senha: str) -> schemas.Token:
    usuario = RepositorioUsuario(session).select_usuario(column="username",
                                                         value=username)

    if not usuario:
        raise errors.erro_400("Usuário ou senha incorretos!")

    if not verificar_senha(senha, usuario.senha):
        raise errors.erro_400("Usuário ou senha incorretos!")

    token = gerar_token({"username": username})
    return schemas.Token(usuario=username, access_token=token)


def validar_dados_de_cadastro(session: Session,
                              schema_usuario: schemas.UsuarioCadastro):
    if _email_ja_cadastrado(session, schema_usuario.email):
        raise errors.erro_400("Email já cadastrado!")

    if _username_ja_cadastrado(session, schema_usuario.username):
        raise errors.erro_400("Username já cadastrado!")

    if _username_muito_grande(schema_usuario.username):
        raise errors.erro_400("Username não pode ter mais de 14 caracteres!")

    return True


def _email_ja_cadastrado(session: Session, email: str) -> bool:
    usuario = RepositorioUsuario(session).select_usuario(column="email",
                                                         value=email)

    if not usuario:
        return False

    return True


def _username_ja_cadastrado(session: Session, username: str) -> bool:
    usuario = RepositorioUsuario(session).select_usuario(column="username",
                                                         value=username)

    if not usuario:
        return False

    return True


def _username_muito_grande(username: str) -> bool:
    if len(username) > 14:
        return True

    return False
