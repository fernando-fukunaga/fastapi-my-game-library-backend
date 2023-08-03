# Módulo de configuração do banco de dados
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_game_library.db"

# Criando uma engine:
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

# Criando uma Session local:
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando a base que será usada para os modelos da aplicação:
Base = declarative_base()


def criar_banco_de_dados():
    """Criar um banco, caso não exista no projeto.

    Detecta todos os modelos (tabelas) do projeto através do declarative_base
    e cria o banco.

    Raises:
        Exception: Erro no funcionamento do ORM.
    """
    Base.metadata.create_all(bind=engine)


def obter_sessao():
    """Instancia uma session.

    Faz o yield dessa sessão para o cliente poder utilizá-la e depois
    retorna aqui para poder fazer session.close.

    Returns:
        Uma session usada para escrita e consulta no banco de dados.

    Raises:
        Exception
    """
    session = SessionLocal()

    try:
        yield session

    finally:
        session.close()
