from flask import Blueprint, render_template

movies = Blueprint('movies', __name__)

@movies.route('/')
def home():
    return render_template('index.html')
