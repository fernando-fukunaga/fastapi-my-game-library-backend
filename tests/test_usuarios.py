import requests

def test_criar_usuarios_retorna_201():
    response = requests.post("http://localhost:8000/usuarios", json={"nome": "Joao",                                                                   
                                                                     "email": "joao@email",
                                                                     "username": "joao",
                                                                     "senha": "senha"})
    esperado = 201

    assert response.status_code == esperado

def test_listar_usuarios_retorna_200():
    response = requests.get("http://localhost:8000/usuarios")
    esperado = 200

    assert response.status_code == esperado