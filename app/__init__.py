from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devsecret")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
