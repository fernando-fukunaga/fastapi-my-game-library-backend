from fastapi import HTTPException

# Erros 400:
erro_400 = HTTPException(status_code=400,
                         detail="Bad request")
erro_400_login_incorreto = HTTPException(status_code=400,
                                         detail="Username ou senha " +
                                         "incorretos!")
erro_400_email_ja_cadastrado = HTTPException(status_code=400,
                                             detail="E-mail já cadastrado!")
erro_400_username_ja_cadastrado = HTTPException(status_code=400,
                                                detail="Username já " +
                                                "cadastrado!")
erro_400_username_muito_grande = HTTPException(status_code=400,
                                               detail="Username excedeu o " +
                                               "limite de caracteres (14)!")

# Erros 401:
erro_401 = HTTPException(status_code=401,
                         detail="Unauthorized")
erro_401_nao_autenticado = HTTPException(status_code=401,
                                         detail="Não autenticado!")
erro_401_token_invalido = HTTPException(status_code=401,
                                        detail="Token inválido!")

# Erros 404:
erro_404 = HTTPException(status_code=404,
                         detail="Not found")
