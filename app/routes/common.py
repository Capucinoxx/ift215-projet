from flask import Blueprint, render_template, redirect, url_for, jsonify, request

common = Blueprint('common', __name__)


@common.route('/')
def index():
    return render_template('index.html')


@common.route('/meditation')
def meditation():
    return render_template('meditation.html')

@common.route('/astuces')
def astuces():
    return render_template('astuces.html')

@common.route('/seance')
def seance():
    return render_template('seance.html')