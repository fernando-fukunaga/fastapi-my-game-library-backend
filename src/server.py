from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_banco_de_dados, get_banco_de_dados
from src.schemas.schemas import Usuario, Plataforma, Jogo
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.plataforma import RepositorioPlataforma
from src.infra.sqlalchemy.repositorios.jogo import RepositorioJogo

criar_banco_de_dados()
app = FastAPI()

@app.post("/usuarios")
def cadastar_usuarios(usuario: Usuario, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).criar(usuario)

@app.get("/usuarios")
def listar_usuarios(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).listar()

@app.get("/usuarios/{id_usuario}")
def obter_usuario(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).obter(id_usuario)

@app.delete("/usuarios/{id_usuario}")
def remover_usuario(id_usuario: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioUsuario(banco_de_dados).remover(id_usuario)

#================================================================================================================

@app.post("/plataformas")
def cadastrar_plataformas(plataforma: Plataforma, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).criar(plataforma)

@app.get("/plataformas")
def listar_plataformas(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).listar()

@app.get("/plataformas/{id_plataforma}")
def obter_plataforma(id_plataforma: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).obter(id_plataforma)

@app.delete("/plataformas/{id_plataforma}")
def remover_plataforma(id_plataforma: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioPlataforma(banco_de_dados).remover(id_plataforma)

#================================================================================================================

@app.post("/jogos")
def cadastrar_jogos(jogo: Jogo, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).criar(jogo)

@app.get("/jogos")
def listar_jogos(banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).listar()

@app.get("/jogos/{id_jogo}")
def obter_jogo(id_jogo: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).obter(id_jogo)

@app.delete("/jogos/{id_jogo}")
def remover_jogo(id_jogo: int, banco_de_dados: Session = Depends(get_banco_de_dados)):
    return RepositorioJogo(banco_de_dados).remover(id_jogo)