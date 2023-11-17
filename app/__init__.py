from flask import Flask
from app.utils import login_manager
from app.routes import setup_routes
from app.database import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @app.route('/ping')
    def ping():
        return 'pong'

    setup_routes(app)

    return app


from app import routes
from app import models
