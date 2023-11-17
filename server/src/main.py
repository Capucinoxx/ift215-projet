from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/ping')
def ping():
  return '<h1>Pong!</h1>'