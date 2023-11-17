from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app.database import db
from app.models import Emotion
from app.utils import check_required_json_data


emotion_calendar = Blueprint('emotion_calendar', __name__)


@emotion_calendar.route('/emotions')
@login_required
@check_required_json_data(['start_date', 'end_date'])
def emotions():
    data = request.json
    start_date = data['start_date']
    end_date = data['end_date']
    
    emotions = (
        Emotion.query.filter_by(user_id=current_user.id)
        .filter(Emotion.date.between(start_date, end_date))
        .all()
    )

    return jsonify({'success': 'Emotions retrieved', 'data': [e.to_dict() for e in emotions]}), 200


@emotion_calendar.route('/emotion', methods=['POST'])
@login_required
@check_required_json_data(['date', 'emotion'])
def add_emotion():
    data = request.json
    date = data['date']
    emotion = data['emotion']

    emotion = Emotion(user_id=current_user.id, date=date, emotion=emotion)
    db.session.add(emotion)
    db.session.commit()

    return jsonify({'success': 'Emotion added', 'data': emotion.to_dict()}), 201


@emotion_calendar.route('/emotion', methods=['DELETE'])
@login_required
@check_required_json_data(['id'])
def remove_emotion():
    pass