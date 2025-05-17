from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from .extensions import db, migrate
from .routes.actors import actors_bp


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(actors_bp, url_prefix='/actors')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Casting Agency API"})

    return app
