# Contem os modelos que representam as entidades do banco
# BOOK representa a entidade BOOK

from uuid import uuid4 
from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID 
from db import db


class Book(db.Model):
# Indica que book é um odelo gerenciado pelo SQLAlchemy
    __tablename__ = "book"
    # Define o nome da tabela
    id = db.Column(
        UUID(as_uuid=True), # Vou usar o UUID
        primary_key = True, # Chave primária
        default = uuid4 # Quando criar um novo livro, um UUID será criado 
    )
    title = db.Column(
        String(255), # Recebe a string
        nullable = False, # Não aceita nulo 
    )
    author = db.Column(
        String(255),
        nullable = False
    )
    # title e author são obrigatórios
    description = db.Column(
        Text, # Textos Maiores
        nullable = False 
    )

    is_favorite = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    is_reading = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )

    is_finished = db.Column(
        db.Boolean,
        nullable = False,
        default = False
    )
    def as_dict(self):
        return{
            "id":str(self.id), # Necessário conversão forçada 
            "title":(self.title),
            "author":(self.author),
            "description":(self.description),
            "is_favorite":(self.is_favorite),
            "is_reading":(self.is_reading),
            "is_finished":(self.is_finished)
        }

# Transformando o modelo em dicionário 

""" 
Por isso, será criado um método responsável por transformar o objeto BOOK em um dicionário python.
Quando ocorre uma consulta ao nosso sistema, ele retorna um objeto book, e ele não é simplesmente um dict python.
O método as_dict() funciona como uma camada de conversão, selecionando apenas o necessário para ser exposto pela API e transformando em um dict,
estrutura que pode ser facilmente serializada para JSON resposta HTTP.
"""
