from flask import Blueprint, render_template
from sqlalchemy import text
from app.controllers.movieController import MovieController
from flask import Flask, request, jsonify

movies = Blueprint('movies', __name__)

@movies.route('/')
def home():
    return render_template('index.html')

@movies.route('/add', methods=['POST'])
def add_movie():
    data = request.json 
    result = MovieController.add_movie(
        name=data['name'],
        description=data.get('description', None),
        release_date=data.get('release_date', None),
        director=data.get('director', None),
        genre=data.get('genre', None)
    )

    return jsonify(message=result)