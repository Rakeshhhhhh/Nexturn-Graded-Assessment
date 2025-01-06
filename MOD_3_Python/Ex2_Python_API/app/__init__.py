from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import main_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object('config.Config')

    # Initialize the database with the app
    db.init_app(app)

    # Register the blueprint
    app.register_blueprint(main_routes)

    return app
