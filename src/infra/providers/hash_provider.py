# Módulo que trata de criptografar e decriptografar as senhas dos usuários.
from passlib.context import CryptContext

# Criando contexto de criptografia e escolhendo o método bcrypt
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def gerar_hash(senha: str) -> str:
    """Função geradora de hash

    Transforma a senha em texto plano do usuário em uma string criptografada
    para que a mesma possa ser salva com segurança no banco de dados.

    Args:
        senha (str): A senha do usuário em texto plano

    Returns:
        Uma string criptografada e ilegível em linguagem humana.

    Raises:
        ValueError: Caso o parâmetro obrigatório não seja informado.
        Exception: Caso ocorra um erro ao gerar o hash.
    """
    return password_context.hash(senha)


def verificar_senha(senha_pura: str, senha_criptografada: str) -> bool:
    """Função verificadora de senha

    Verifica se a senha digitada pelo usuário ao tentar o login está
    correta de acordo com a senha criptografada que está no banco de
    dados.

    Args:
        senha_pura (str): A senha do usuário em texto plano
        senha_criptografada (str): A senha criptografada retirada do
            banco de dados.

    Returns:
        True caso a senha esteja correta e False caso não esteja.

    Raises:
        ValueError: Caso os parâmetros obrigatórios não sejam informados.
        Exception: Caso ocorra um erro ao verificar a senha.
    """
    return password_context.verify(senha_pura, senha_criptografada)
