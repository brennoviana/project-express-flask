from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .routes.movieRoutes import movies
    app.register_blueprint(movies, url_prefix='/movies')

    return app
