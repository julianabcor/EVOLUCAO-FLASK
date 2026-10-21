# Responsável pela aplicação flask e pelos endpoits
# App de gerenciamento de livros
# Consultar 
# Editar
# Atualizar
# Deletar
# Favoritar
# Livros em leitura
# Livros finalizados

from flask import flask 
from db import db 
from dotenv import load_dotenv
import os 

load_dotenv() # Carrega o .env
app = flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database")