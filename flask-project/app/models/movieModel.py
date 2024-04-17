from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    director = db.Column(db.String(100), nullable=True)
    genre = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f'<Movie {self.name}>'
