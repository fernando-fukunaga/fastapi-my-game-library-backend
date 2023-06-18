from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    username: str
    senha: str
    plataformas: List[Plataforma]
    jogos: List[Jogo]

class Plataforma(BaseModel):
    id: Optional[int] = None
    nome: str
    usuario: Usuario
    fabricante: str
    observacoes: Optional[str] = "Sem observações"
    jogos: List[Jogo]

class Jogo(BaseModel):
    id: int
    nome: str
    plataforma: Plataforma
    ano: int
    categoria: str
    desenvolvedora: str
    usuario: Usuario
    observacoes: Optional[str] = "Sem observações"
    status: str
    