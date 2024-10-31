from src.services.services_auth import criar_usuario, autenticar


def signup_endpoint(request):
    return criar_usuario(request)

def login_endpoint(request):
    return autenticar(request)
