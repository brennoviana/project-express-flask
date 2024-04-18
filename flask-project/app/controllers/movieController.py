from app import db
from app.models.movieModel import Movie
from datetime import date
from flask import request

class MovieController:
    @staticmethod
    def get_all_movies():
        try:
            all_movies = Movie.query.all()
            return all_movies, 200  
        except Exception as e:
            return f'Error: {str(e)}', 500 


    @staticmethod
    def add_movie(name, description, release_date, director, genre):
        new_movie = Movie(
            name=name,
            description=description,
            release_date=date.fromisoformat(release_date) if release_date else None,
            director=director,
            genre=genre
        )
        db.session.add(new_movie)
        try:
            db.session.commit()
            return f'Filme "{name}" adicionado com sucesso!', 201
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}', 500
        

    @staticmethod
    def delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            return 'Filme não encontrado!', 404

        try:
            db.session.delete(movie)
            db.session.commit()
            return f'Filme "{movie.name}" deletado com sucesso', 200
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}', 500
        
    @staticmethod
    def get_movie(user_id):
        try:
            movie = Movie.query.get(user_id)
            return movie, 200  
        except Exception as e:
            return f'Error: {str(e)}', 500
        

    @staticmethod
    def update_movie(movie_id):
        try:
            movie = Movie.query.get(movie_id)
            if not movie:
                return "Filme não encontrado", 404
            
            for field, value in request.form.items():
                if hasattr(movie, field):
                    if value == '':
                        continue
                    setattr(movie, field, value)

            db.session.commit()

            return f'Filme "{movie.name}" alterado com sucesso!', 200
    
        except Exception as e:
            return f'Error: {str(e)}', 500