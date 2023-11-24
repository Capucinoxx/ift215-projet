from flask import Blueprint, render_template, request, jsonify, url_for, send_from_directory
from flask_login import current_user, login_required
from app.database import db
from app.models import Emotion
from app.utils import check_required_json_data
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


emotion_calendar = Blueprint('emotion_calendar', __name__)


@emotion_calendar.route('/emotions', methods=['GET'])
@login_required
def emotions():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        now = datetime.now()
        start_date = now - timedelta(days=now.weekday())
        end_date = start_date + timedelta(days=6)
    else:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    emotions = []
    if start_date and end_date:
        emotions = (
            Emotion.query.filter_by(user_id=current_user.id)
            .filter(Emotion.date.between(start_date, end_date))
            .all()
        )

    emotion_dict = {}

    for emotion in emotions:
        emotion_date = emotion['date']
        emotion_content = emotion['content']
        emotion_dict[emotion_date] = emotion_content

    emotions = [{'date': (start_date + timedelta(days=i)).strftime('%Y-%m-%d'), 'emotion': emotion_dict.get((start_date + timedelta(days=i)).strftime('%Y-%m-%d'), '')} for i in range(7)]


    next_week = f"/emotions?start_date={end_date + timedelta(days=1):%Y-%m-%d}&end_date={end_date + timedelta(days=7):%Y-%m-%d}"
    prev_week = f"/emotions?start_date={start_date - timedelta(days=7):%Y-%m-%d}&end_date={start_date - timedelta(days=1):%Y-%m-%d}"

    return render_template('journalisation.html', emotions=emotions, 
                           start_date=start_date, end_date=end_date, 
                           week_number=start_date.isocalendar()[1],
                           next_week=next_week, previous_week=prev_week)

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
    