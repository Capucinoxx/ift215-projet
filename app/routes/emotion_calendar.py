from flask import Blueprint
from app.utils import check_required_json_data

emotion_calendar = Blueprint('emotion_calendar', __name__)


@emotion_calendar.route('/emotions')
@check_required_json_data(['start_date', 'end_date'])
def emotions():
    pass


@emotion_calendar.route('/emotion', methods=['POST', 'DELETE'])
def emotion():
    pass