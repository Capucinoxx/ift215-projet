from .auth import auth
from .emotion_calendar import emotion_calendar


def setup_routes(app):
    app.register_blueprint(auth)
    app.register_blueprint(emotion_calendar)
