from pydantic import BaseModel
from typing import Optional

#===========REQUESTS===============

class JogoCadastro(BaseModel):
    nome: str
    id_plataforma: int
    ano: int
    categoria: str
    desenvolvedora: str
    id_usuario: int
    observacoes: Optional[str] = "Sem observações"
    progresso: float
    
    class Config:
        orm_mode = True

#===========RESPONSES===============

class JogoDadosSimples(BaseModel):
    id: int
    nome: str
    id_plataforma: int
    ano: int
    categoria: str
    desenvolvedora: str
    id_usuario: int
    observacoes: str
    progresso: float

    class Config:
        orm_mode = True