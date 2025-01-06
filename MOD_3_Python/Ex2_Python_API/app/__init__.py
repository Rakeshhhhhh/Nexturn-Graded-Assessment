from flask import Flask
from .extensions import db  # Import db from extensions
from .routes import main_routes

def create_app():
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object('config.Config')

    # Initialize extensions with the app
    db.init_app(app)

    # Register the blueprint
    app.register_blueprint(main_routes)

    return app
