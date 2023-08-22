from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils.paperfly_encryption import create_config_with_encryption_key

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    create_config_with_encryption_key()

    db.init_app(app)
    migrate.init_app(app, db)

    # Registra el blueprint
    from app.notebook_execution import bp as notebook_execution_bp
    app.register_blueprint(notebook_execution_bp, url_prefix='/notebook')

    # Registra el blueprint de repositorio
    from app.repo import bp as repo_bp
    app.register_blueprint(repo_bp, url_prefix='/repo')

    return app