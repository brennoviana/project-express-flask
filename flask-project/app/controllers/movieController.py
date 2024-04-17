from app.database import db
from app.models.movieModel import Movie
from datetime import date

class MovieController:
    @staticmethod
    def get_movie():
        return "Movies"

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
            return f'Filme "{name}" adicionado com sucesso!'
        except Exception as e:
            db.session.rollback()
            return f'Error: {str(e)}'
