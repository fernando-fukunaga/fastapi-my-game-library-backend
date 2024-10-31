# Schemas, modelos para input e output, views da API
from pydantic import BaseModel
from typing import List, Optional

# ===========REQUESTS===============


class UsuarioCadastro(BaseModel):
    nome: str
    email: str
    username: str
    senha: str

    class Config:
        orm_mode = True


class PlataformaCadastro(BaseModel):
    nome: str
    fabricante: str
    observacoes: Optional[str] = "Sem observações"

    class Config:
        orm_mode = True


class JogoCadastro(BaseModel):
    nome: str
    id_plataforma: int
    ano: int
    categoria: str
    desenvolvedora: str
    observacoes: Optional[str] = "Sem observações"
    progresso: float

    class Config:
        orm_mode = True


class JogoPut(BaseModel):
    nome: str
    ano: int
    categoria: str
    desenvolvedora: str
    observacoes: Optional[str] = "Sem observações"
    progresso: float

    class Config:
        orm_mode = True

# ===========RESPONSES===============


class UsuarioDadosSimples(BaseModel):
    id: int
    nome: str
    email: str
    username: str

    class Config:
        orm_mode = True


class PlataformaDadosSimples(BaseModel):
    id: int
    nome: str
    fabricante: str
    observacoes: str

    class Config:
        orm_mode = True


class JogoDadosSimples(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str
    observacoes: str
    progresso: float

    class Config:
        orm_mode = True


class PlataformaDadosDetalhados(BaseModel):
    id: int
    nome: str
    fabricante: str
    observacoes: str
    jogos: List[JogoDadosSimples]

    class Config:
        orm_mode = True


class JogoDadosDetalhados(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str
    desenvolvedora: str
    observacoes: str
    progresso: float
    plataforma: PlataformaDadosSimples

    class Config:
        orm_mode = True


class Token(BaseModel):
    usuario: str
    access_token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True
