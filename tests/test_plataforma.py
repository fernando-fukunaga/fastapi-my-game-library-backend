# Testes para endpoints de plataforma
from fastapi.testclient import TestClient
from src.main import app

"""Criando um testclient para fazer requisições sem precisar subir o servidor,
isso aumenta muito o desempenho dos testes, ele usa o HTTPX
por baixo dos panos:"""
client = TestClient(app)

# Token fixo para o usuário fernando, sem expiração, para testes:
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZlcm5hbmRvIiwidmFsaWRhZGUiOiIxMy8wNy8yMDIzLCAxOTo0OToxOSJ9.ozwDM63scHmWLy5mXpADw7NVdSjF1nvUVVJRahTDH3w"
headers = {"Authorization": f"Bearer {TOKEN}"}


class TestPlataforma:

    def test_criar_plataforma_retorna_201(self):
        response = client.post(url="/plataformas",
                               json={"nome": "Test",
                                     "fabricante": "Test"},
                               headers=headers)

        assert response.status_code == 201

    def test_listar_plataformas_retorna_200(self):
        response = client.get(url="/plataformas",
                              headers=headers)

        assert response.status_code == 200

    def test_obter_plataforma_existente_retorna_200(self):
        response = client.get(url="/plataformas/1",
                              headers=headers)

        assert response.status_code == 200

    def test_obter_plataforma_inexistente_retorna_404(self):
        response = client.get(url="/plataformas/0",
                              headers=headers)

        assert response.status_code == 404

    def test_obter_plataforma_com_string_retorna_422(self):
        response = client.get(url="/plataformas/a",
                              headers=headers)

        assert response.status_code == 422

    def test_atualizar_plataforma_corretamente_retorna_200(self):
        response = client.put(url="/plataformas/3",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 200

    def test_atualizar_plataforma_inexistente_retorna_404(self):
        response = client.put(url="/plataformas/0",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 404

    def test_atualizar_plataforma_existente_mas_nao_pertencente_ao_usuario_logado_retorna_404(self):
        response = client.put(url="/plataformas/2",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 404

    def test_atualizar_plataforma_com_string_retorna_422(self):
        response = client.put(url="/plataformas/a",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 422

    def test_deletar_plataforma_corretamente_retorna_204(self):
        response = client.delete(url="/plataformas/3",
                                 headers=headers)

        assert response.status_code == 204

    def test_deletar_plataforma_inexistente_retorna_404(self):
        response = client.delete(url="/plataformas/0",
                                 headers=headers)

        assert response.status_code == 404

    def test_deletar_plataforma_existente_mas_nao_pertencente_ao_usuario_logado_retorna_404(self):
        response = client.delete(url="/plataformas/2",
                                 headers=headers)

        assert response.status_code == 404

    def test_deletar_plataforma_com_string_retorna_422(self):
        response = client.delete(url="/plataformas/a",
                                 headers=headers)

        assert response.status_code == 422
