# Testes para endpoints de plataforma
from tests.config import client, headers, mock_user_model
from unittest.mock import patch, MagicMock

mock_plataforma_model = MagicMock(
    id=1,
    nome="Test",
    id_usuario=1,
    fabricante="Test",
    observacoes="Test"
)
mock_plataforma_alheia_model = MagicMock(
    id=2,
    nome="Test",
    id_usuario=2,
    fabricante="Test",
    observacoes="Test"
)
patch_select_usuario_for_authentication = "src.utils.auth_utils.RepositorioUsuario.select_usuario"
patch_insert_plataforma = "src.services.services_plataforma.RepositorioPlataforma.insert_plataforma"
patch_select_plataforma = "src.services.services_plataforma.RepositorioPlataforma.select_plataforma"
patch_select_plataformas = "src.services.services_plataforma.RepositorioPlataforma.select_plataformas"
patch_update_plataforma = "src.services.services_plataforma.RepositorioPlataforma.update_plataforma"
patch_delete_plataforma = "src.services.services_plataforma.RepositorioPlataforma.delete_plataforma"


class TestPlataforma:

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_insert_plataforma)
    def test_criar_plataforma_retorna_201(self, mock_insert,
                                          mock_authenticate):
        mock_insert.return_value = mock_plataforma_model
        mock_authenticate.return_value = mock_user_model

        response = client.post(url="/plataformas",
                               json={"nome": "Test",
                                     "fabricante": "Test"},
                               headers=headers)

        mock_insert.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 201

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataformas)
    def test_listar_plataformas_retorna_200(self, mock_select,
                                            mock_authenticate):
        mock_select.return_value = [mock_plataforma_model]
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/plataformas",
                              headers=headers)

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    def test_obter_plataforma_existente_retorna_200(self, mock_select,
                                                    mock_authenticate):
        mock_select.return_value = mock_plataforma_model
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/plataformas/1",
                              headers=headers)

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    def test_obter_plataforma_inexistente_retorna_404(self, mock_select,
                                                      mock_authenticate):
        mock_select.return_value = None
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/plataformas/1",
                              headers=headers)

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    @patch(patch_select_usuario_for_authentication)
    def test_obter_plataforma_com_string_retorna_422(self, mock_authenticate):
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/plataformas/a",
                              headers=headers)

        mock_authenticate.assert_called_once()
        assert response.status_code == 422

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    @patch(patch_update_plataforma)
    def test_atualizar_plataforma_corretamente_retorna_200(self, mock_update,
                                                           mock_select,
                                                           mock_authenticate):
        mock_authenticate.return_value = mock_user_model
        mock_select.return_value = mock_plataforma_model
        mock_update.return_value = mock_plataforma_model

        response = client.put(url="/plataformas/1",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        mock_select.assert_called_once()
        mock_update.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    def test_atualizar_plataforma_inexistente_ou_nao_pertencente_ao_usuario_logado_retorna_404(
            self,
            mock_select,
            mock_authenticate
    ):
        mock_authenticate.return_value = mock_user_model
        mock_select.return_value = None

        response = client.put(url="/plataformas/1",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    @patch(patch_select_usuario_for_authentication)
    def test_atualizar_plataforma_com_string_retorna_422(self, mock_authenticate):
        mock_authenticate.return_value = mock_user_model

        response = client.put(url="/plataformas/a",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        mock_authenticate.assert_called_once()
        assert response.status_code == 422

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    @patch(patch_delete_plataforma)
    def test_deletar_plataforma_corretamente_retorna_204(self, mock_delete,
                                                         mock_select,
                                                         mock_authenticate):
        mock_authenticate.return_value = mock_user_model
        mock_select.return_value = mock_plataforma_model
        mock_delete.return_value = None

        response = client.delete(url="/plataformas/1",
                                 headers=headers)

        mock_delete.assert_called_once()
        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 204

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataforma)
    def test_deletar_plataforma_inexistente_ou_nao_pertencente_ao_usuario_logado_retorna_404(
        self,
        mock_select,
        mock_authenticate
    ):
        mock_authenticate.return_value = mock_user_model
        mock_select.return_value = None

        response = client.delete(url="/plataformas/1",
                                 headers=headers)

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    @patch(patch_select_usuario_for_authentication)
    def test_deletar_plataforma_com_string_retorna_422(self, mock_authenticate):
        mock_authenticate.return_value = mock_user_model

        response = client.delete(url="/plataformas/a",
                                 headers=headers)

        mock_authenticate.assert_called_once()
        assert response.status_code == 422
