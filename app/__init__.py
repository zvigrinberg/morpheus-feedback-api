from flask import Flask
from .routes import register_routes


def create_app():
    app = Flask(__name__)

    # Load configuration from app/config.py
    app.config.from_object('app.config.Config')

    # Initialize the Argilla SDK
    from .sdk import init_argilla
    init_argilla(app)

    # Register API endpoints
    register_routes(app)

    return app
