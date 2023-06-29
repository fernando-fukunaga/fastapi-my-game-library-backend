from pydantic import BaseModel
from typing import List
from src.schemas.schemas_plataforma import PlataformaDadosSimples
from src.schemas.schemas_jogo import JogoDadosSimples

#===========REQUESTS===============

class UsuarioCadastro(BaseModel):
    nome: str
    email: str
    username: str
    senha: str

    class Config:
        orm_mode = True

#===========RESPONSES===============     
   
class UsuarioDadosSimples(BaseModel):
    id: int
    nome: str
    email: str
    username: str
    plataformas: List[PlataformaDadosSimples]
    jogos: List[JogoDadosSimples]

    class Config:
        orm_mode = True