# Módulo responsável por gerar e verificar JWTs
from jose import jwt
from datetime import datetime, timedelta

# JWT Config:
SECRET_KEY = "b6bb9d2def7db1e0999898609fb99c4c07b95a121f5d0c7e2ed0cd4e84c4d7c2"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 60


def gerar_token(payload: dict) -> str:
    """Função para gerar o token a partir do payload.

    Args:
        payload (dict): A carga usada para gerar o JWT, utiliza-se
            nessa aplicação, o username.

    Returns:
        Um JWT em forma de string

    Raises:
        ValueError: Caso o parâmetro obrigatório não seja informado.
        Exception: Caso ocorra um erro ao gerar o token.
    """

    # Criando cópia do payload para adicionar a expiração do token:
    copia_payload = payload.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    copia_payload.update({"exp": expiracao})

    # Cria o token:
    token = jwt.encode(copia_payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verificar_token(token: str):
    """Função para fazer o decode do JWT e retornar o username encontrado.

    Args:
        token (str): O token passado no header da requisição.

    Returns:
        Uma string com o username atrelado ao token.

    Raises:
        ValueError: Caso o parâmetro obrigatório não seja informado.
        JWTError: Caso ocorra um erro ao verificar o token.
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    return payload.get("username")
