# Testes para endpoints de Jogo
from tests.config import client, headers
from unittest.mock import patch, MagicMock


class TestJogo:

    def test_criar_jogo_retorna_201(self):
        response = client.post(url="/jogos",
                               json={"nome": "Test",
                                     "id_plataforma": 1,
                                     "ano": 2000,
                                     "categoria": "Test",
                                     "desenvolvedora": "Test",
                                     "progresso": 50.0},
                               headers=headers)

        assert response.status_code == 201

    def test_listar_jogos_retorna_200(self):
        response = client.get(url="/jogos",
                              headers=headers)

        assert response.status_code == 200

    def test_obter_jogo_existente_retorna_200(self):
        response = client.get(url="/jogos/1",
                              headers=headers)

        assert response.status_code == 200

    def test_obter_jogo_inexistente_retorna_404(self):
        response = client.get(url="/jogos/0",
                              headers=headers)

        assert response.status_code == 404

    def test_obter_jogo_existente_mas_nao_pertencente_ao_usuario_retorna_404(self):
        response = client.get(url="/jogos/7",
                              headers=headers)

        assert response.status_code == 404

    def test_obter_jogo_com_string_retorna_422(self):
        response = client.get(url="/jogos/a",
                              headers=headers)

        assert response.status_code == 422

    def test_atualizar_jogo_corretamente_retorna_200(self):
        response = client.put(url="/jogos/2",
                              headers=headers,
                              json={"nome": "Test",
                                    "id_plataforma": 1,
                                    "ano": 2000,
                                    "categoria": "Test",
                                    "desenvolvedora": "Test",
                                    "progresso": 50.0})

        assert response.status_code == 200

    def test_atualizar_jogo_inexistente_retorna_404(self):
        response = client.put(url="/jogos/0",
                              headers=headers,
                              json={"nome": "Test",
                                    "id_plataforma": 1,
                                    "ano": 2000,
                                    "categoria": "Test",
                                    "desenvolvedora": "Test",
                                    "progresso": 50.0})

        assert response.status_code == 404

    def test_atualizar_jogo_com_string_retorna_422(self):
        response = client.put(url="/jogos/a",
                              headers=headers,
                              json={"nome": "Test",
                                    "fabricante": "Test"})

        assert response.status_code == 422

    def test_deletar_jogo_corretamente_retorna_204(self):
        response = client.delete(url="/jogos/2",
                                 headers=headers)

        assert response.status_code == 204

    def test_deletar_jogo_inexistente_retorna_404(self):
        response = client.delete(url="/jogos/0",
                                 headers=headers)

        assert response.status_code == 404

    def test_deletar_jogo_com_string_retorna_422(self):
        response = client.delete(url="/jogos/a",
                                 headers=headers)

        assert response.status_code == 422
