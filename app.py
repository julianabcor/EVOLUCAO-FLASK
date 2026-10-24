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
from flask_migrate import Migrate
from models.book import Book

load_dotenv() # Carrega o .env
app = flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("database")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)