from pydantic import BaseModel
from typing import Optional

#===========REQUESTS===============

class PlataformaCadastro(BaseModel):
    nome: str
    id_usuario: int
    fabricante: str
    observacoes: Optional[str] = "Sem observações"
    
    class Config:
        orm_mode = True

#===========RESPONSES===============

class PlataformaDadosSimples(BaseModel):
    id: int
    nome: str
    id_usuario: str
    fabricante: str
    observacoes: str
    
    class Config:
        orm_mode = True