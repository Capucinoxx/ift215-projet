from flask import Blueprint, render_template, request, jsonify, url_for, send_from_directory
from flask_login import current_user, login_required
from app.database import db
from app.models import Emotion
from app.utils import check_required_json_data
from werkzeug.utils import secure_filename



emotion_calendar = Blueprint('emotion_calendar', __name__)


@emotion_calendar.route('/emotions', methods=['GET'])
@login_required
def emotions():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    emotions = []
    if start_date and end_date:
        emotions = (
            Emotion.query.filter_by(user_id=current_user.id)
            .filter(Emotion.date.between(start_date, end_date))
            .all()
        )


    return render_template('journalisation.html', emotions=emotions)


@emotion_calendar.route('/emotion', methods=['POST'])
@login_required
@check_required_json_data(['date', 'emotion'])
def add_emotion():
    data = request.json
    date = data['date']
    emotion = data['emotion']

    try:
        emotion = Emotion(user_id=current_user.id, date=date, emotion=emotion)
        db.session.add(emotion)
        db.session.commit()
    except:
        return jsonify({'error': 'Bad insertion'}), 400

    return jsonify({'success': 'Emotion added', 'data': emotion.to_dict()}), 201


@emotion_calendar.route('/emotion', methods=['DELETE'])
@login_required
@check_required_json_data(['id'])
def remove_emotion():
    data = request.json
    emotion_id = data['id']

    try:
        emotion = Emotion.query.filter_by(id=emotion_id, user_id=current_user.id).first()
    except:
        return jsonify({'error': 'Bad insertion'}), 400
    
    if not emotion:
        return jsonify({'error': 'Emotion not found'}), 404
    
    db.session.delete(emotion)
    db.session.commit()

    return jsonify({'success': 'Emotion removed', 'data': emotion.to_dict()}), 200

@emotion_calendar.route('/emotions/<emotion_name>', methods=['GET'])
def show_emotion(emotion_name):
    emotion = secure_filename(emotion_name)
    directory = 'static/emotions'
    return send_from_directory(directory, emotion), 200
    