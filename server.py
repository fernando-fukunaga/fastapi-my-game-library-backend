from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_banco_de_dados, get_banco_de_dados
from src.schemas import schemas_usuario
from src.schemas import schemas_plataforma
from src.schemas import schemas_jogo
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.repositorio_plataforma import RepositorioPlataforma
from src.infra.sqlalchemy.repositorios.repositorio_jogo import RepositorioJogo

criar_banco_de_dados()
app = FastAPI()

@app.post("/usuarios", response_model=schemas_usuario.UsuarioDadosSimples)
def cadastar_usuarios(usuario: schemas_usuario.UsuarioCadastro, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).criar(usuario)

@app.get("/usuarios", response_model=List[schemas_usuario.UsuarioDadosSimples])
def listar_usuarios(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).listar()

@app.get("/usuarios/{id_usuario}", response_model=schemas_usuario.UsuarioDadosSimples)
def obter_usuario(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).obter(id_usuario)

@app.delete("/usuarios/{id_usuario}")
def remover_usuario(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).remover(id_usuario)

#================================================================================================================

@app.post("/plataformas", response_model=schemas_plataforma.PlataformaDadosSimples)
def cadastrar_plataformas(plataforma: schemas_plataforma.PlataformaCadastro, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).criar(plataforma)

@app.get("/plataformas", response_model=List[schemas_plataforma.PlataformaDadosSimples])
def listar_plataformas(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).listar()

@app.get("/plataformas/{id_plataforma}", response_model=schemas_plataforma.PlataformaDadosSimples)
def obter_plataforma(id_plataforma: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).obter(id_plataforma)

@app.delete("/plataformas/{id_plataforma}")
def remover_plataforma(id_plataforma: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).remover(id_plataforma)

#================================================================================================================

@app.post("/jogos", response_model=schemas_jogo.JogoDadosSimples)
def cadastrar_jogos(jogo: schemas_jogo.JogoCadastro, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).criar(jogo)

@app.get("/jogos", response_model=List[schemas_jogo.JogoDadosSimples])
def listar_jogos(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).listar()

@app.get("/jogos/{id_jogo}", response_model=schemas_jogo.JogoDadosSimples)
def obter_jogo(id_jogo: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).obter(id_jogo)

@app.delete("/jogos/{id_jogo}")
def remover_jogo(id_jogo: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).remover(id_jogo)