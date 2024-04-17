from flask import Flask
from app.config import Config
from app.database import db
from app.models import movieModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.movieRoutes import movies
    app.register_blueprint(movies, url_prefix='/movie')

    with app.app_context():
        db.create_all() 

    return app
