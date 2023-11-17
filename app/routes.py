from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.models import User
from app.utils import check_required_json_data


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'success': 'Logged out'}), 200


@app.route('/register', methods=['GET', 'POST'])
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
