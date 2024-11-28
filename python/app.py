from flask import Flask
from app.routes import register_blueprints

def create_app():
    app = Flask(__name__)

    # Register blueprints
    register_blueprints(app)

    return app
