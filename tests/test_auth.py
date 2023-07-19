from src.main import create_app
from fastapi.testclient import TestClient
from unittest import mock
from sqlalchemy import create_engine


def mock_engine():
    return create_engine("sqlite://",
                         connect_args={"check_same_thread": False})


@mock.patch("src.infra.sqlalchemy.config.database.engine",
            mock_engine)
def test_criar_usuario_retorna_200():
    client = TestClient(create_app())
    response = client.post(url="/auth/signup",
                           json={"nome": "Felipe",
                                 "email": "felipe1@email",
                                 "username": "felipe1",
                                 "senha": "senha"})

    assert response.status_code == 201
