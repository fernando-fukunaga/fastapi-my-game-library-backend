import requests


def test_listar_usuarios_retorna_200():
    response = requests.get("http://localhost:8000/usuarios")
    esperado = 200

    assert response.status_code == esperado
