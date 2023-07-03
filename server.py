from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_banco_de_dados, criar_sessao
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import RepositorioPlataforma
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo

criar_banco_de_dados()
app = FastAPI()


@app.post("/usuarios", response_model=schemas.UsuarioDadosSimples, status_code=201)
async def cadastar_usuario(usuario: schemas.UsuarioCadastro, session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).criar(usuario)


@app.get("/usuarios", response_model=List[schemas.UsuarioDadosSemLista])
async def listar_usuarios(session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).listar()


@app.get("/usuarios/{id_usuario}", response_model=schemas.UsuarioDadosSimples)
async def obter_usuario(id_usuario: int, session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).obter(id_usuario)


@app.put("/usuarios/{id_usuario}", response_model=schemas.UsuarioDadosSimples)
async def atualizar_usuario(id_usuario: int, usuario: schemas.UsuarioCadastro, session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).atualizar(id_usuario, usuario)


@app.delete("/usuarios/{id_usuario}")
async def remover_usuario(id_usuario: int, session: Session = Depends(criar_sessao)):
    return RepositorioUsuario(session).remover(id_usuario)

# ================================================================================================================


@app.post("/plataformas", response_model=schemas.PlataformaDadosSimples, status_code=201)
async def cadastrar_plataforma(plataforma: schemas.PlataformaCadastro, session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).criar(plataforma)


@app.get("/plataformas", response_model=List[schemas.PlataformaDadosSemLista])
async def listar_plataformas(session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).listar()


@app.get("/plataformas/{id_plataforma}", response_model=schemas.PlataformaDadosSimples)
async def obter_plataforma(id_plataforma: int, session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).obter(id_plataforma)


@app.delete("/plataformas/{id_plataforma}")
async def remover_plataforma(id_plataforma: int, session: Session = Depends(criar_sessao)):
    return RepositorioPlataforma(session).remover(id_plataforma)

# ================================================================================================================


@app.post("/jogos", response_model=schemas.JogoDadosSimples, status_code=201)
async def cadastrar_jogo(jogo: schemas.JogoCadastro, session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).criar(jogo)


@app.get("/jogos", response_model=List[schemas.JogoDadosSemLista])
async def listar_jogos(session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).listar()


@app.get("/jogos/{id_jogo}", response_model=schemas.JogoDadosSimples)
async def obter_jogo(id_jogo: int, session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).obter(id_jogo)


@app.delete("/jogos/{id_jogo}")
async def remover_jogo(id_jogo: int, session: Session = Depends(criar_sessao)):
    return RepositorioJogo(session).remover(id_jogo)
