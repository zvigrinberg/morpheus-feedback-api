from flask import Flask
from .routes import register_routes
from .sdk import init_argilla

def create_app():
    app = Flask(__name__)

    # Load configuration from app/config.py
    app.config.from_object('app.config.Config')

    # Initialize the Argilla SDK
    init_argilla(app)
    print("Argilla SDK initialized successfully.")

# Register API endpoints
    register_routes(app)

    return app
