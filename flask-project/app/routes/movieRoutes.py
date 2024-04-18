from flask import Blueprint, render_template, redirect, url_for, flash
from app.controllers.movieController import MovieController
from flask import request, jsonify

movie = Blueprint('movie', __name__)

from flask import render_template

@movie.route('/', methods=['GET'])
def main_movie():
    movies, status = MovieController.get_all_movies()
    if status == 200:
        return render_template('index.html', movies=movies)
    else:
        return render_template('index.html', error="Falha ao carregar filmes.")


@movie.route('/getAll', methods=['GET'])
def list_movies():
    movies, status = MovieController.get_all_movies()
    
    if status == 200:  
        movies_list = [
            {
                'id': movie.id,
                'name': movie.name,
                'description': movie.description,
                'release_date': movie.release_date.isoformat() if movie.release_date else None,
                'director': movie.director,
                'genre': movie.genre
            } for movie in movies
        ]
        return jsonify(movies_list), 200
    else:
        return jsonify({'message': movies}), status


@movie.route('/add', methods=['POST'])
def add_movie():
    data = request.get_json()
    result, status = MovieController.add_movie(
        name=data['name'],
        description=data.get('description', None),
        release_date=data.get('release_date', None),
        director=data.get('director', None),
        genre=data.get('genre', None)
    )

    if status == 201:
        flash('success', 'Filme adicionado com sucesso!')  
        return jsonify(message=result), status
    elif status == 409:
        flash('error', 'Filme ja existe!')  
        return jsonify(message=result), status
    flash('error', 'Erro ao adicionar filme!')  
    return jsonify(message=result), status



@movie.route('/delete/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    message, status = MovieController.delete_movie(int(movie_id))
    if status == 200:
        flash('error', 'Filme deletado com sucesso!') 
        return jsonify(message=message), status
    flash('error', 'Erro ao deletar filme!')  
    return jsonify(message=message), status


@movie.route('form-update/<int:movie_id>', methods=['GET', 'POST'])
def update_movie_form(movie_id):
    if request.method == "GET":
        result, status = MovieController.get_movie(int(movie_id)) 
        if status == 200:
            return render_template('update_movie.html', movie=result)
        return jsonify(message=result), status

    result, status = MovieController.update_movie(int(movie_id))
    if status == 200:
        flash('success', 'Filme atualizado com sucesso!')  
        return redirect(url_for('movie.main_movie'))  
    flash('error', 'Erro ao atualizar filme!')  
    return render_template('update_movie.html', movie=result)
