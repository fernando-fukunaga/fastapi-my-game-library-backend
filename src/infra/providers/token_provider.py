from jose import jwt
from datetime import datetime, timedelta

# JWT Config:
SECRET_KEY = "b6bb9d2def7db1e0999898609fb99c4c07b95a121f5d0c7e2ed0cd4e84c4d7c2"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 60


def gerar_token(payload: dict):
    copia_payload = payload.copy()

    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    expiracao_formatada = expiracao.strftime("%d/%m/%Y, %H:%M:%S")

    copia_payload.update({"validade": expiracao_formatada})

    token = jwt.encode(copia_payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verificar_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)

    return payload.get("username")
