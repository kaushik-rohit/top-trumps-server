from flask import jsonify
from app import app
import db

@app.route('/game/<int:game_id>/<int:round_num>', methods=['GET'])
def text_query(game_id, round_num):
    return jsonify(db.card_query(game_id, round_num))

