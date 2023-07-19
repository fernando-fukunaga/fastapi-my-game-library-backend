from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import routers_auth, routers_plataforma, routers_jogo
from src.infra.sqlalchemy.config.database import criar_banco_de_dados


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(routers_auth.router)
    app.include_router(routers_plataforma.router)
    app.include_router(routers_jogo.router)

    criar_banco_de_dados()

    return app


app = create_app()

origins = ["http://localhost:8000"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
