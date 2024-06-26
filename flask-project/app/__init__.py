from flask import Flask
from app.config import Config
from app.database import db
from app.models import movieModel
from app.filters import register_filters

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.movieRoutes import movie
    app.register_blueprint(movie, url_prefix='/movie')

    with app.app_context():
        db.create_all() 

    register_filters(app)
    
    return app
