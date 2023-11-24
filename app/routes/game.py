from flask import Blueprint, render_template

clicker_game = Blueprint('game', __name__)

@clicker_game.route('/game', methods=['GET'])
def game():
    return render_template('clicker_game.html')