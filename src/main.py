"""Módulo responsável por inicializar a aplicação.

Esse módulo é o módulo principal da aplicação, o qual o servidor utiliza
para levantar a mesma, criar o banco de dados se o mesmo não estiver criado
e configura middlewares para receber requisições de qualquer origem.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routers_auth, routers_plataforma, routers_jogo, router_home
from src.infra.sqlalchemy.config.database import criar_banco_de_dados


def create_app() -> FastAPI:
    """Função para criar e configurar a aplicação.

    Instancia a aplicação FastAPI, inclui as rotas e cria o banco de dados.

    Returns:
        Uma instância da aplicação para ser usada pelo servidor.

    Raises:
        Exception: Caso haja algum problema ao levantar o app ou ao se
        conectar com o banco de dados.
    """
    app = FastAPI()
    app.include_router(routers_auth.router)
    app.include_router(routers_plataforma.router)
    app.include_router(routers_jogo.router)
    app.include_router(router_home.router)

    criar_banco_de_dados()

    return app


app = create_app()

# Configuração de middlewares:
origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
