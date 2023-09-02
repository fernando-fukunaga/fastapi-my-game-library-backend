# Rota home:
from fastapi import APIRouter

# Criando router para o endpoint home, para melhorar o Swagger:
router = APIRouter(tags=["Home"])


@router.get("/")
async def rota_padrao():
    return {"mensagem":"A aplicação está funfando!"}
