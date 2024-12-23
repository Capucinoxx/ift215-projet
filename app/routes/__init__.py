from .auth import auth
from .emotion_calendar import emotion_calendar
from .common import common
from .game import clicker_game


def setup_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(emotion_calendar)
    app.register_blueprint(common)
    app.register_blueprint(clicker_game)
