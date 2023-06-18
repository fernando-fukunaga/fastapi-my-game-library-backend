from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    username: str
    senha: str

class Plataforma(BaseModel):
    id: Optional[int] = None
    nome: str
    id_usuario: int
    fabricante: str
    observacoes: Optional[str] = "Sem observações"
    
class Jogo(BaseModel):
    id: Optional[int] = None
    nome: str
    id_plataforma: int
    ano: int
    categoria: str
    desenvolvedora: str
    id_usuario: int
    observacoes: Optional[str] = "Sem observações"
    status: str