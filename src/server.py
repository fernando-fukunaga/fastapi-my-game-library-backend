from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_banco_de_dados, get_banco_de_dados
from src.schemas.schemas import Usuario, Plataforma
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.plataforma import RepositorioPlataforma

criar_banco_de_dados()
app = FastAPI()

@app.post("/cadastrar-usuarios")
def cadastar(usuario: Usuario, banco_de_dados: Session = Depends(get_banco_de_dados)):
    usuario_cadastrado = RepositorioUsuario(banco_de_dados).criar(usuario)
    return usuario_cadastrado

@app.get("/listar-usuarios")
def listar(banco_de_dados: Session = Depends(get_banco_de_dados)):
    lista_usuarios = RepositorioUsuario(banco_de_dados).listar()
    return lista_usuarios

@app.post("/cadastrar-plataformas")
def cadastrar_plataformas(plataforma: Plataforma, banco_de_dados: Session = Depends(get_banco_de_dados)):
    plataforma_cadastrada = RepositorioPlataforma(banco_de_dados).criar(plataforma)
    return plataforma_cadastrada

@app.get("/listar-plataformas")
def listar_plataformas(banco_de_dados: Session = Depends(get_banco_de_dados)):
    lista_plataformas = RepositorioPlataforma(banco_de_dados).listar()
    return lista_plataformas