<div align="center">
  <img src="docs/images/mgl-logo.jpg" alt="" width=320>
  <p><strong>MyGameLibrary: An API to manage yout video games!</strong></p>

  ![Static Badge](https://img.shields.io/badge/Status-Vers%C3%A3o%20beta%20dispon%C3%ADvel-green)
</div>

MyGameLibrary is a REST API, developed by me, in Python, using the web framework FastAPI.

It's currently in beta version, more improved versions are on their way. I've created this project with studying purposes, to learn backend development concepts and stuff. Therefore, the repository is open for issues and pull requests, but, I'm always going to review them and see if they make sense in my learning path. Because I like to always know what every line of code is doing and, concepts that are too advanced may be an obstacle in the process.

## 🤔 How does the application work?
On MyGameLibrary, the users have to sign up, and then sign in to the API. The authentication system is made via OAuth2, the login endpoint will be returning an access token, which the user has to pass in the Authorization header of every subsequent request, with the string "Bearer " as a prefix. The header value will look like this: "Bearer \<access_token\>". If you're consuming the API via Swagger UI (available in the "/docs" endpoint), you don't need to worry about that part, just click in the "Authenticate" button and input your credentials.

After registering and singing in, the user can register all the platforms where they play video games, it can be a Playstation, a Nintendo, a computer, anything. Every registered platform will have an ID number that points to the logged in user. And than the user can register the specific games of each platform, inputting data like the name, the year, the category, and the most important thing, the progress.

That's because the intention is to offer to the user a game management platform, where they can get a good view of all of their games, how many of them are finished, how many are incomplete, how many are not even started, etc. And then the user can organize themselves, decide in what order they want to finish their games, keep track of the progress, and things like that.

Just a reminder that, MyGameLibrary can work as a BFF (backend for frontend), so feel free to create a frontend application to consume it 😊.

## 👨🏻‍💻 Development information
The application was developed under the REST parttern. I used the Python programming language and the FastAPI framework, this framework has become very popular for being asynchornous, using an ASGI server, in contrast to Flask or Django.

I used for this application, a MVC-like architecture, just changing the name of the components. The models are still being called models, the views are composed by routers (definition of the endpoints) and schemas (base model for data input/output using JSON), and the controllers are being called repositories.

* DBMS used: SQLite
* Testing: unit tests with Pytest

## 💻 How do I run this project on my computer?
To run o MyGameLibrary em sua máquina, você precisa das seguintes ferramentas:
* Python 3.11.x instalado na máquina;
* Um terminal PowerShell;
* Um navegador web ou programas de teste de API como Postman ou Insomnia.

Agora é só seguir os passos abaixo:
### 1. Baixar o clonar o projeto em sua máquina
Você pode fazer o download do .zip do projeto ou usar o git clone para clonar em sua máquina (assim pode até sugerir contribuições).

### 2. Instalar os pacotes necessários
No terminal, preferencialmente PowerShell, execute o comando abaixo para instalar os pacotes necessários:
```powershell
pip install -r requirements.txt
```

### 3. Subir o servidor
Execute o comando abaixo, no diretório raíz do projeto, para subir o servidor uvicorn com a aplicação:
```powershell
uvicorn src.main:app
```

### 4. Checar o Swagger
Após subir a aplicação no localhost, acesse o Swagger pela url http:localhost:*porta*/docs. Pelo Swagger você poderá conferir todos os endpoints da aplicação e já testar por lá mesmo. Faça o seu cadastro e divirta-se!

## 🚀 Deploy
A versão beta ainda não será deployada na web, pois ainda estou estudando e aprendendo conteinerização com Docker e procurando o melhor serviço de hospedagem para mim. Nas próximas versões, será possível testar minha API diretamente do seu navegador ou utilizando ferramentas famosas como o Postman.

### Project owner:
| [<img src="https://avatars.githubusercontent.com/u/112123011?s=400&u=22ad423853238139b7091769db66445e54a7e678&v=4" width=115><br><sub>Fernando Fukunaga</sub>](https://github.com/fernando-fukunaga) |
| :---: |
