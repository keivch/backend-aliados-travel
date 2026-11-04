import os

from flask_cors import CORS

from flask import Flask

from app.config import config_by_name
from app.routes.sort_routes import sort_bp
from app.routes.uppercase_routes import uppercase_bp


def create_app(config_name=None):
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

    env_name = config_name or os.environ.get("FLASK_ENV", "development")
    app.config.from_object(config_by_name.get(env_name, config_by_name["development"]))
    app.register_blueprint(sort_bp, url_prefix="/api")
    app.register_blueprint(uppercase_bp, url_prefix="/api")

    return app
