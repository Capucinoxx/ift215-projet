from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .main import main

db = SQLAlchemy()

def create_app(config_file='src.config'):
  app = Flask(__name__)
  app.config.from_object(config_file)
  db.init_app(app)

  app.register_blueprint(main)

  return app