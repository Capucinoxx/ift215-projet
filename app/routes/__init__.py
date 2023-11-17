from .auth import auth


def setup_routes(app):
    app.register_blueprint(auth)
