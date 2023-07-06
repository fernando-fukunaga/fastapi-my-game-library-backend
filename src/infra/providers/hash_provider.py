from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash(senha: str):
    return password_context.hash(senha)


def verificar_senha(senha_pura: str, senha_criptografada: str):
    return password_context.verify(senha_pura, senha_criptografada)
