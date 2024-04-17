from flask import Blueprint, render_template
from sqlalchemy import text
from app.controllers.movieController import MovieController
from flask import Flask, request, jsonify

movies = Blueprint('movies', __name__)

@movies.route('/getAll', methods=['GET'])
def list_movies():
    movies = MovieController.get_all_movies()
    movies_list = [
        {
            'id': movie.id,
            'name': movie.name,
            'description': movie.description,
            'release_date': movie.release_date.isoformat() if movie.release_date else None,
            'director': movie.director,
            'genre': movie.genre
        } for movie in movies
    ] if isinstance(movies, list) else []

    return jsonify(movies_list)


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