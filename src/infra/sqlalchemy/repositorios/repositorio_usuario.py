# Módulo para interações com a tabela de usuarios do banco
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.providers.hash_provider import gerar_hash, verificar_senha
from src.infra.providers.token_provider import gerar_token
from src.errors import errors


class RepositorioUsuario:
    """Classe de interações com o banco de dados.

    Exemplo de instânciação:

    repositorio = RepositorioUsuario(session)

    Attributes:
        session (Session): sessão do SQLAlchemy para escrita e leitura
        no nosso banco.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def verifica_email_ja_cadastrado(self, email: str) -> bool:
        """Função que verifica se o email informado no cadastro
        já existe no banco de dados, pois é um dado UNIQUE.

        Args:
            email (str): o e-mail que o user informa ao tentar se
                cadastrar

        Returns:
            True se o email existir no banco e False se não existir

        Raises:
            ValueError: se o parâmetro obrigatório não for informado.
            Exception: caso haja erro de conexão envolvendo o ORM.
        """
        if self.session.query(models.Usuario).filter_by(email=email).first():
            return True
        return False

    def verifica_username_ja_cadastrado(self, username: str) -> bool:
        """Função que verifica se o username informado no cadastro
        já existe no banco de dados, pois é um dado UNIQUE.

        Args:
            username (str): o username que o user informa ao tentar se
                cadastrar

        Returns:
            True se o username existir no banco e False se não existir

        Raises:
            ValueError: se o parâmetro obrigatório não for informado.
            Exception: caso haja erro de conexão envolvendo o ORM.
        """
        if self.session.query(models.
                              Usuario).filter_by(username=username).first():
            return True
        return False

    def verifica_username_muito_grande(self, username: str) -> bool:
        """Função que verifica se o username informado no cadastro
        possui mais de 14 chars, que é o limite suportado pelo banco.

        Args:
            username (str): o username que o user informa ao tentar se
                cadastrar

        Returns:
            True se o username for muito longo e False se não for

        Raises:
            ValueError: se o parâmetro obrigatório não for informado.
            Exception: caso haja erro de conexão envolvendo o ORM.
        """
        if len(username) > 14:
            return True
        return False

    def criar(self,
              schema_usuario: schemas.UsuarioCadastro) -> models.Usuario:
        """Cria um usuário e insere-o no banco de dados usando o ORM

        Args:
            schema_usuario (UsuarioCadastro): schema para cadastro de
                usuarios, passado pelo user em JSON.

        Returns:
            Um objeto de models.Usuario, caso o cadastro ocorrer bem.
            Esse objeto será convertido em schema para exibição na
            definição da rota.

        Raises:
            erro_400: caso o cadastro seja feito desrespeitando as
                regras de negócio e repetindo valores unique.
        """
        if self.verifica_email_ja_cadastrado(schema_usuario.email):
            raise errors.erro_400("E-mail já cadastrado!")

        if self.verifica_username_ja_cadastrado(schema_usuario.username):
            raise errors.erro_400("Username já cadastrado!")

        if self.verifica_username_muito_grande(schema_usuario.username):
            raise errors.erro_400(
                "Username excedeu limite de caracteres (14)")

        model_usuario = models.Usuario(nome=schema_usuario.nome,
                                       email=schema_usuario.email,
                                       username=schema_usuario.username,
                                       senha=gerar_hash(schema_usuario.senha))

        self.session.add(model_usuario)
        self.session.commit()
        self.session.refresh(model_usuario)
        return model_usuario

    def obter_por_username(self, username: str) -> models.Usuario:
        """Pesquisa usuário no banco a partir de seu username

        Args:
            username (str): username para pesquisa

        Returns:
            Um objeto de models.Usuario, se a busca for bem-sucedida e
            None se for mal-sucedida.

        Raises:
            ValueError: caso o parâmetro obrigatório não seja informado
            Exception: caso haja um problema com o ORM durante execução
        """
        return self.session.query(
            models.Usuario).filter_by(username=username).first()

    def autenticar(self, username: str, senha: str) -> schemas.Token:
        """Realiza a autenticação para o endpoint do login

        Args:
            username (str): username para login
            senha (str): senha para login

        Returns:
            Um schema para mostrar o token ao usuario.

        Raises:
            erro_400: se o username ou senha estiverem incorretos.
        """
        model_usuario = self.obter_por_username(username)

        if not model_usuario:
            raise errors.erro_400("Usuário ou senha incorretos!")

        if not verificar_senha(senha, model_usuario.senha):
            raise errors.erro_400("Usuário ou senha incorretos!")

        token = gerar_token({"username": username})

        return schemas.Token(usuario=model_usuario, access_token=token)
