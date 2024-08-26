# Testes para endpoints de autenticação
from tests.config import client, password_context, headers, mock_user_model
from unittest.mock import patch, MagicMock

patch_insert_usuario_in_services = "src.services.services_auth.RepositorioUsuario.insert_usuario"
patch_select_usuario_in_services = "src.services.services_auth.RepositorioUsuario.select_usuario"
patch_select_usuario_for_authentication = "src.utils.auth_utils.RepositorioUsuario.select_usuario"


class TestSignUp:

    @patch(patch_insert_usuario_in_services)
    @patch(patch_select_usuario_in_services)
    def test_criar_usuario_corretamente_retorna_201(self, mock_select, mock_insert):
        mock_insert.return_value = mock_user_model
        mock_select.return_value = None

        response = client.post(url="/auth/signup",
                               json={"nome": "test",
                                     "email": "test",
                                     "username": "test",
                                     "senha": "test"})

        mock_select.assert_called()
        mock_insert.assert_called_once()
        assert response.status_code == 201

    @patch(patch_select_usuario_in_services)
    def test_criar_usuario_com_email_ou_username_existentes_retorna_400(self, mock_select):
        mock_select.return_value = mock_user_model

        response = client.post(url="/auth/signup",
                               json={"nome": "test",
                                     "email": "test",
                                     "username": "test",
                                     "senha": "test"})

        mock_select.assert_called()
        assert response.status_code == 400

    @patch(patch_select_usuario_in_services)
    def test_criar_usuario_com_username_maior_que_14_chars_retorna_400(self, mock_select):
        mock_select.return_value = None

        response = client.post(url="/auth/signup",
                               json={"nome": "test",
                                     "email": "test",
                                     "username": "test00000000000",
                                     "senha": "test"})

        mock_select.assert_called()
        assert response.status_code == 400


class TestLogin:

    @patch(patch_select_usuario_in_services)
    def test_tentar_login_com_usuario_existente_retorna_200(self, mock_select):
        mock_select.return_value = mock_user_model

        response = client.post(url="/auth/login",
                               data={"username": "test",
                                     "password": "test"})

        mock_select.assert_called()
        assert response.status_code == 200 

    @patch(patch_select_usuario_in_services)
    def test_tentar_login_com_usuario_inexistente_retorna_400(self, mock_select):
        mock_select.return_value = None

        response = client.post(url="/auth/login",
                               data={"username": "test",
                                     "password": "test"})

        mock_select.assert_called()
        assert response.status_code == 400

    @patch(patch_select_usuario_in_services)
    def test_tentar_login_com_senha_incorreta_retorna_400(self, mock_select):
        mock_select.return_value = mock_user_model

        response = client.post(url="/auth/login",
                               data={"username": "test",
                                     "password": "test0"})

        mock_select.assert_called()
        assert response.status_code == 400


class TestMe:

    @patch(patch_select_usuario_for_authentication)
    def test_rota_me_com_token_valido_retorna_200(self, mock_select):
        mock_select.return_value = mock_user_model

        response = client.get(url="/auth/me", headers=headers)

        mock_select.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    def test_rota_me_com_token_invalido_retorna_401(self, mock_select):
        mock_select.return_value = None

        response = client.get(url="/auth/me", headers={"Authorization": ""})

        assert response.status_code == 401
