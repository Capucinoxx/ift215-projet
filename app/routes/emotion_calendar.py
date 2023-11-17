from flask import Blueprint, request, jsonify
from flask_login import current_user
from app.models import Emotion
from app.utils import check_required_json_data


emotion_calendar = Blueprint('emotion_calendar', __name__)


@emotion_calendar.route('/emotions')
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


@emotion_calendar.route('/emotion', methods=['POST', 'DELETE'])
def emotion():
    pass