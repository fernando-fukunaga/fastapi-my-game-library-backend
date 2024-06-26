# Testes para endpoints de autenticação
from tests.config import client, password_context, headers
from unittest.mock import patch, MagicMock


class TestSignUp:

    @patch("src.services.services_auth.RepositorioUsuario.insert_usuario")
    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_criar_usuario_corretamente_retorna_201(self, mock_select, mock_insert):
        mock_user_model = MagicMock(nome='daniel',
                                    email='daniel',
                                    username='daniel',
                                    senha='daniel')
        mock_insert.return_value = mock_user_model
        mock_select.return_value = None

        response = client.post(url="/auth/signup",
                               json={"nome": "daniel",
                                     "email": "daniel",
                                     "username": "daniel",
                                     "senha": "daniel"})

        mock_select.assert_called()
        mock_insert.assert_called_once()
        assert response.status_code == 201

    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_criar_usuario_com_email_ou_username_existentes_retorna_400(self, mock_select):
        mock_user_model = MagicMock(nome='daniel',
                                    email='daniel',
                                    username='daniel',
                                    senha='daniel')
        mock_select.return_value = mock_user_model

        response = client.post(url="/auth/signup",
                               json={"nome": "daniel",
                                     "email": "daniel",
                                     "username": "daniel",
                                     "senha": "daniel"})

        mock_select.assert_called()
        assert response.status_code == 400

    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_criar_usuario_com_username_maior_que_14_chars_retorna_400(self, mock_select):
        mock_select.return_value = None
        response = client.post(url="/auth/signup",
                               json={"nome": "daniel",
                                     "email": "daniel",
                                     "username": "daniel000000000",
                                     "senha": "daniel"})

        mock_select.assert_called()
        assert response.status_code == 400


class TestLogin:

    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_tentar_login_com_usuario_existente_retorna_200(self, mock_select):
        mock_user_model = MagicMock(nome='daniel',
                                    email='daniel',
                                    username='daniel',
                                    senha=password_context.hash('daniel'))
        mock_select.return_value = mock_user_model
        
        response = client.post(url="/auth/login",
                               data={"username": "daniel",
                                     "password": "daniel"})

        mock_select.assert_called()
        assert response.status_code == 200 

    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_tentar_login_com_usuario_inexistente_retorna_400(self, mock_select):
        mock_select.return_value = None
        
        response = client.post(url="/auth/login",
                               data={"username": "daniel",
                                     "password": "daniel"})

        mock_select.assert_called()
        assert response.status_code == 400

    @patch("src.services.services_auth.RepositorioUsuario.select_usuario")
    def test_tentar_login_com_senha_incorreta_retorna_400(self, mock_select):
        mock_user_model = MagicMock(nome='daniel',
                                    email='daniel',
                                    username='daniel',
                                    senha=password_context.hash('daniel'))
        mock_select.return_value = mock_user_model

        response = client.post(url="/auth/login",
                               data={"username": "daniel",
                                     "password": "daniel0"})

        assert response.status_code == 400


class TestMe:

    @patch("src.utils.auth_utils.RepositorioUsuario.select_usuario")
    def test_rota_me_com_token_valido_retorna_200(self, mock_select):
        mock_user_model = MagicMock(nome='fernando',
                                    email='fernando',
                                    username='fernando',
                                    senha=password_context.hash('fernando'))
        mock_select.return_value = mock_user_model
        
        response = client.get(url="/auth/me", headers=headers)

        mock_select.assert_called_once()
        assert response.status_code == 200

    def test_rota_me_com_token_invalido_retorna_401(self):
        response = client.get(url="/auth/me", headers={"Authorization": ""})

        assert response.status_code == 401
