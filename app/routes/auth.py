from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_user, logout_user, current_user, login_required
from app.database import db
from app.models import User
from app.utils import check_required_json_data

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
@check_required_json_data(['username', 'password'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('ping'))

    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401

    login_user(user, remember=True)

    return jsonify({'success': 'Logged in', 'data': user.to_dict()}), 200


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': 'Logged out'}), 200


@auth.route('/register', methods=['GET', 'POST'])
@check_required_json_data(['username', 'password'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('ping'))

    data = request.json
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already taken'}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'success': 'Registered', 'data': user.to_dict()}), 201
