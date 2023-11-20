from __future__ import annotations


from app.utils import login_manager
from app.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f"User('{self.username}')"

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
        }


class Emotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, nullable=False)
    emotion = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"Emotion('{self.user_id}', '{self.date}', '{self.emotion}')"
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'date': self.date,
            'emotion': self.emotion,
        }