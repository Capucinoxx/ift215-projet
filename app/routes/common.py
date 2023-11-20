from flask import Blueprint, render_template, redirect, url_for, jsonify, request

common = Blueprint('common', __name__)


@common.route('/')
def index():
    return render_template('index.html')