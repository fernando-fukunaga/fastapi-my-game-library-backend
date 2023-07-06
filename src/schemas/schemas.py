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


class UsuarioLogin(BaseModel):
    username: str
    senha: str

    class Config:
        orm_mode = True


class PlataformaCadastro(BaseModel):
    nome: str
    id_usuario: int
    fabricante: str
    observacoes: Optional[str] = "Sem observações"

    class Config:
        orm_mode = True


class PlataformaPut(BaseModel):
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


class UsuarioDadosSemLista(BaseModel):
    id: int
    nome: str
    email: str
    username: str

    class Config:
        orm_mode = True


class PlataformaDadosSemLista(BaseModel):
    id: int
    nome: str
    fabricante: str
    observacoes: str

    class Config:
        orm_mode = True


class JogoDadosSemLista(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str
    observacoes: str
    progresso: float

    class Config:
        orm_mode = True


class PlataformaDadosParaUsuarioSimples(BaseModel):
    id: int
    nome: str
    fabricante: str
    observacoes: str
    jogos: List[JogoDadosSemLista]

    class Config:
        orm_mode = True


class UsuarioDadosSimples(BaseModel):
    id: int
    nome: str
    email: str
    username: str
    plataformas: List[PlataformaDadosParaUsuarioSimples]

    class Config:
        orm_mode = True


class PlataformaDadosSimples(BaseModel):
    id: int
    nome: str
    fabricante: str
    observacoes: str
    usuario: UsuarioDadosSemLista
    jogos: List[JogoDadosSemLista]

    class Config:
        orm_mode = True


class JogoDadosSimples(BaseModel):
    id: int
    nome: str
    ano: int
    categoria: str
    desenvolvedora: str
    observacoes: str
    progresso: float
    plataforma: PlataformaDadosSemLista

    class Config:
        orm_mode = True


class Token(BaseModel):
    mensagem = "Autenticado com sucesso!"
    username: str
    access_token = "token"

    class Config:
        orm_mode = True
