# Testes para endpoints de autenticação
from fastapi.testclient import TestClient
from src.main import app
from tests.gerador_numeros import gera_numero

"""Criando um testclient para fazer requisições sem precisar subir o servidor,
isso aumenta muito o desempenho dos testes, ele usa o HTTPX
por baixo dos panos:"""
client = TestClient(app)

# Token fixo para o usuário fernando, sem expiração, para testes:
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImZlcm5hbmRvIiwidmFsaWRhZGUiOiIxMy8wNy8yMDIzLCAxOTo0OToxOSJ9.ozwDM63scHmWLy5mXpADw7NVdSjF1nvUVVJRahTDH3w"
headers = {"Authorization": f"Bearer {TOKEN}"}


class TestSignUp:

    def test_criar_usuario_retorna_201(self):
        response = client.post(url="/auth/signup",
                               json={"nome": "Test Dummy",
                                     "email": f"test{gera_numero()}@email.com",
                                     "username": f"test{gera_numero()}",
                                     "senha": "senha"})

        assert response.status_code == 201

    def test_criar_usuario_com_email_existente_retorna_400(self):
        response = client.post(url="/auth/signup",
                               json={"nome": "Test Dummy",
                                     "email": "fernando@email.com",
                                     "username": f"test{gera_numero()}",
                                     "senha": "senha"})

        assert response.status_code == 400

    def test_criar_usuario_com_username_existente_retorna_400(self):
        response = client.post(url="/auth/signup",
                               json={"nome": "Test Dummy",
                                     "email": f"test{gera_numero()}@email.com",
                                     "username": "fernando",
                                     "senha": "senha"})

        assert response.status_code == 400

    def test_criar_usuario_com_username_maior_que_14_chars_retorna_400(self):
        response = client.post(url="/auth/signup",
                               json={"nome": "Test Dummy",
                                     "email": f"test{gera_numero()}@email.com",
                                     "username": "test11111111111",
                                     "senha": "senha"})

        assert response.status_code == 400


class TestLogin:

    def test_tentar_login_com_usuario_existente_retorna_200(self):
        response = client.post(url="/auth/login",
                               data={"username": "fernando",
                                     "password": "senha"})

        assert response.status_code == 200

    def test_tentar_login_com_usuario_inexistente_retorna_400(self):
        response = client.post(url="/auth/login",
                               data={"username": "usuario_inexistente",
                                     "password": "senha"})

        assert response.status_code == 400

    def test_tentar_login_com_senha_incorreta_retorna_400(self):
        response = client.post(url="/auth/login",
                               data={"username": "fernando",
                                     "password": "senha1"})

        assert response.status_code == 400


class TestMe:

    def test_rota_me_com_token_valido_retorna_200(self):
        response = client.get(url="/auth/me", headers=headers)

        assert response.status_code == 200

    def test_rota_me_com_token_invalido_retorna_401(self):
        response = client.get(url="/auth/me", headers={"Authorization": ""})

        assert response.status_code == 401
