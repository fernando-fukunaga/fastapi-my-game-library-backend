# Testes para endpoints de Jogo
import src.infra.sqlalchemy.repositorios.repositorio_jogo
from tests.config import client, headers, mock_user_model
from unittest.mock import patch, MagicMock

mock_jogo_model = MagicMock(
    id=1,
    nome="Test",
    id_plataforma=1,
    ano=2000,
    categoria="Test",
    desenvolvedora="Test",
    progresso=50.0,
    observacoes="Test"
)
mock_plataforma_model = MagicMock(
    id=1,
    nome="Test",
    id_usuario=1,
    fabricante="Test",
    observacoes="Test"
)
mock_jogo_model.plataforma = mock_plataforma_model
patch_select_usuario_for_authentication = "src.utils.auth_utils.RepositorioUsuario.select_usuario"
patch_insert_jogo = "src.services.services_jogo.RepositorioJogo.insert_jogo"
patch_select_jogo = "src.services.services_jogo.RepositorioJogo.select_jogo"
patch_select_jogos = "src.services.services_jogo.RepositorioJogo.select_jogos"
patch_update_jogo = "src.services.services_jogo.RepositorioJogo.update_jogo"
patch_delete_jogo = "src.services.services_jogo.RepositorioJogo.delete_jogo"
patch_select_plataformas = "src.services.services_jogo.RepositorioPlataforma.select_plataformas"


class TestJogo:
    @patch(patch_select_usuario_for_authentication)
    @patch(patch_insert_jogo)
    @patch(patch_select_plataformas)
    def test_criar_jogo_corretamente_retorna_201(self, mock_select, mock_insert,
                                                 mock_authenticate):
        mock_insert.return_value = mock_jogo_model
        mock_select.return_value = [mock_plataforma_model]
        mock_authenticate.return_value = mock_user_model

        response = client.post(url="/jogos",
                               json={"nome": "Test",
                                     "id_plataforma": 1,
                                     "ano": 2000,
                                     "categoria": "Test",
                                     "desenvolvedora": "Test",
                                     "progresso": 50.0},
                               headers=headers)

        mock_insert.assert_called_once()
        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 201

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_jogos)
    @patch(patch_select_plataformas)
    def test_listar_jogos_retorna_200(self, mock_select_plataformas,
                                      mock_select_jogos, mock_authenticate):
        mock_select_plataformas.return_value = [mock_plataforma_model]
        mock_select_jogos.return_value = [mock_jogo_model]
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/jogos",
                              headers=headers)

        mock_select_plataformas.assert_called_once()
        mock_select_jogos.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_jogo)
    @patch(patch_select_plataformas)
    def test_obter_jogo_existente_retorna_200(self, mock_select_plataformas,
                                              mock_select_jogo, mock_authenticate):
        mock_select_plataformas.return_value = [mock_plataforma_model]
        mock_select_jogo.return_value = mock_jogo_model
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/jogos/1",
                              headers=headers)

        mock_select_plataformas.assert_called_once()
        mock_select_jogo.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_jogo)
    def test_obter_jogo_inexistente_retorna_404(self, mock_select, mock_authenticate):
        mock_select.return_value = None
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/jogos/0",
                              headers=headers)

        mock_select.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_jogo)
    @patch(patch_select_plataformas)
    def test_obter_jogo_existente_mas_nao_pertencente_ao_usuario_logado_retorna_404(
        self,
        mock_select_plataformas,
        mock_select_jogo,
        mock_authenticate
    ):
        mock_plataforma_alheia_model = MagicMock(
            id=2,
            nome="Test",
            id_usuario=2,
            fabricante="Test",
            observacoes="Test"
        )

        mock_select_jogo.return_value = mock_jogo_model
        mock_select_plataformas.return_value = [mock_plataforma_alheia_model]
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/jogos/1",
                              headers=headers)

        mock_select_jogo.assert_called_once()
        mock_select_plataformas.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    @patch(patch_select_usuario_for_authentication)
    def test_obter_jogo_com_string_retorna_422(self, mock_authenticate):
        mock_authenticate.return_value = mock_user_model

        response = client.get(url="/jogos/a",
                              headers=headers)

        mock_authenticate.assert_called_once()
        assert response.status_code == 422

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_update_jogo)
    @patch(patch_select_plataformas)
    @patch(patch_select_jogos)
    def test_atualizar_jogo_corretamente_retorna_200(self, mock_select_jogos,
                                                     mock_select_plataformas,
                                                     mock_update,
                                                     mock_authenticate):
        mock_select_plataformas.return_value = [mock_plataforma_model]
        mock_select_jogos.return_value = [mock_jogo_model]
        mock_update.return_value = mock_jogo_model
        mock_authenticate.return_value = mock_user_model

        response = client.put(url="/jogos/1",
                              headers=headers,
                              json={"nome": "Test",
                                    "id_plataforma": 1,
                                    "ano": 2000,
                                    "categoria": "Test",
                                    "desenvolvedora": "Test",
                                    "progresso": 50.0})

        mock_update.assert_called_once()
        mock_select_plataformas.assert_called_once()
        mock_select_jogos.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 200

    @patch(patch_select_usuario_for_authentication)
    @patch(patch_select_plataformas)
    @patch(patch_select_jogos)
    def test_atualizar_jogo_inexistente_ou_nao_pertencente_ao_usuario_logado_retorna_404(
        self,
        mock_select_jogos,
        mock_select_plataformas,
        mock_authenticate
    ):
        mock_select_plataformas.return_value = [mock_plataforma_model]
        mock_select_jogos.return_value = None
        mock_authenticate.return_value = mock_user_model

        response = client.put(url="/jogos/1",
                              headers=headers,
                              json={"nome": "Test",
                                    "id_plataforma": 1,
                                    "ano": 2000,
                                    "categoria": "Test",
                                    "desenvolvedora": "Test",
                                    "progresso": 50.0})

        mock_select_plataformas.assert_called_once()
        mock_select_jogos.assert_called_once()
        mock_authenticate.assert_called_once()
        assert response.status_code == 404

    def test_atualizar_jogo_com_string_retorna_422(self):
        response = client.put(url="/jogos/a",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 422

    @patch("src.services.services_jogo.RepositorioJogo.delete_jogo")
    def test_deletar_jogo_corretamente_retorna_204(self, mock_delete):
        mock_delete.return_value = None

        response = client.delete(url="/jogos/1",
                                 headers=headers)

        mock_delete.assert_called_once()
        assert response.status_code == 204

    def test_deletar_jogo_inexistente_retorna_404(self):
        response = client.delete(url="/jogos/0",
                                 headers=headers)

        assert response.status_code == 404

    def test_deletar_jogo_existente_mas_nao_pertencente_ao_usuario_logado_retorna_404(self):
        response = client.delete(url="/jogos/2",
                                 headers=headers)

        assert response.status_code == 404

    def test_deletar_jogo_com_string_retorna_422(self):
        response = client.delete(url="/jogos/a",
                                 headers=headers)

        assert response.status_code == 422
