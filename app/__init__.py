from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS (if the frontend is hosted separately)
    CORS(app)

    # Initialize plugins
    db.init_app(app)

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
