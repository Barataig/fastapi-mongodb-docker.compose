# fastapi-mongodb-docker.compose

FastAPI MongoDB API

API de exemplo utilizando FastAPI com MongoDB, incluindo operações CRUD de usuários.

Estrutura do projeto

app/

init.py

main.py : Ponto de entrada da API

crud.py : Operações CRUD

db.py : Conexão com MongoDB

requirements.txt

Dockerfile

Requisitos

Python 3.12+

pip

MongoDB (local ou Docker)

Docker (opcional, para containerização)

Instalação

Clone o projeto:
git clone <REPO_URL>
cd fastapi-mongo

Crie um virtualenv (Windows):
python -m venv .venv
..venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt
ou individualmente: pip install fastapi uvicorn pymongo

Rodando localmente

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

Acesse no navegador:
http://127.0.0.1:8000

Rodando via Docker

Construir a imagem:
docker build -t fastapi-mongo-api .

Rodar containers:
MongoDB:
docker run -d -p 27017:27017 --name fastapi-mongo mongo:6.0

API FastAPI:
docker run -d -p 8000:8000 --name fastapi_api --link fastapi-mongo fastapi-mongo-api

Acesse no navegador:
http://localhost:8000

Endpoints de exemplo

GET / : Mensagem de teste

GET /users : Lista usuários

POST /users : Criar usuário

GET /users/{id}: Obter usuário por ID

PUT /users/{id}: Atualizar usuário

DELETE /users/{id}: Deletar usuário

Referências

FastAPI Docs: https://fastapi.tiangolo.com/

PyMongo Docs: https://pymongo.readthedocs.io/

Docker Docs: https://docs.docker.com/
