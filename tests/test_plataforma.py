# Testes para endpoints de autenticação
from fastapi.testclient import TestClient
from src.main import app

"""Criando um testclient para fazer requisições sem precisar subir o servidor,
isso aumenta muito o desempenho dos testes, ele usa o HTTPX
por baixo dos panos:"""
client = TestClient(app)

# Token fixo para o usuário fernando, sem expiração, para testes:
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZlcm5hbmRvIiwidmFsaWRhZGUiOiIxMy8wNy8yMDIzLCAxOTo0OToxOSJ9.ozwDM63scHmWLy5mXpADw7NVdSjF1nvUVVJRahTDH3w"


class TestPlataforma:

    def test_criar_plataforma_retorna_201(self):
        response = client.post(url="/plataformas",
                               json={"nome": "Test",
                                     "fabricante": "Test"},
                               headers={"Authorization": f"Bearer {TOKEN}"})

        assert response.status_code == 201

    def test_listar_plataformas_retorna_200(self):
        response = client.get(url="/plataformas",
                               headers={"Authorization": f"Bearer {TOKEN}"})

        assert response.status_code == 200

    def test_obter_plataforma_retorna_200(self):
        response = client.get(url="/plataformas/1",
                               headers={"Authorization": f"Bearer {TOKEN}"})

        assert response.status_code == 200
