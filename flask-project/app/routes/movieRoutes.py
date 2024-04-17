from flask import Blueprint, render_template
from app import db
from sqlalchemy import text

movies = Blueprint('movies', __name__)

@movies.route('/')
def home():
    return render_template('index.html')

@movies.route('/test_db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return "Conexão com o banco de dados está funcionando!"
    except Exception as e:
        return f"Erro ao conectar com o banco de dados: {e}"