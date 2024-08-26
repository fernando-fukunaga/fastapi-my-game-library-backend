# Configurações e constantes usadas para testes
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from src.main import app
from passlib.context import CryptContext

# Criando contexto de bcrypt para senhas de usuarios mockados
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

"""Criando um testclient para fazer requisições sem precisar subir o servidor,
isso aumenta muito o desempenho dos testes, ele usa o HTTPX
por baixo dos panos:"""
client = TestClient(app)

# Token fixo genérico, sem expiração, para testes:
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3QifQ.HZ7pjkqB5ZsF4Ocw-0qr89Yt5OwsZ5pFokt13aUqdxY"
headers = {"Authorization": f"Bearer {TOKEN}"}

mock_user_model = MagicMock(id=1,
                            nome='test',
                            email='test',
                            username='test',
                            senha=password_context.hash('test'))
