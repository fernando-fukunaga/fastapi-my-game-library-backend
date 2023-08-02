import requests

prefixo = "http://localhost:8000"


class TestSignUp:
    def test_criar_usuario_retorna_201(self):
        response = requests.post(url=prefixo+"/auth/signup",
                                 json={"nome": "John Doe",
                                       "email": "john.doe@email.com",
                                       "username": "john.doe",
                                       "senha": "senha"})

        assert response.status_code == 201

    def test_criar_usuario_com_mesmo_email_retorna_400(self):
        response = requests.post(url=prefixo+"/auth/signup",
                                 json={"nome": "John Doe",
                                       "email": "john.doe@email.com",
                                       "username": "john.doe",
                                       "senha": "senha"})

        assert response.status_code == 400

    def test_criar_usuario_com_mesmo_username_retorna_400(self):
        response = requests.post(url=prefixo+"/auth/signup",
                                 json={"nome": "John Doe",
                                       "email": "john.doe1@email.com",
                                       "username": "john.doe",
                                       "senha": "senha"})

        assert response.status_code == 400

    def test_criar_usuario_com_username_maior_que_14_chars_retorna_400(self):
        response = requests.post(url=prefixo+"/auth/signup",
                                 json={"nome": "John Doe",
                                       "email": "john.doe1@email.com",
                                       "username": "john.doe1111111",
                                       "senha": "senha"})

        assert response.status_code == 400


class TestLogin:
    def test_tentar_login_com_usuario_existente_retorna_200(self):
        response = requests.post(url=prefixo+"/auth/login",
                                 data={"username": "john.doe",
                                       "senha": "senha"})

        assert response.status_code == 200

    def test_tentar_login_com_usuario_inexistente_retorna_400(self):
        response = requests.post(url=prefixo+"/auth/login",
                                 data={"username": "john.doe1",
                                       "password": "senha"})

        assert response.status_code == 400
