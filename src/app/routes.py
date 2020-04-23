from flask import jsonify, request
from flask_cors import cross_origin
from app import app
import db


@app.route('/game/<int:game_id>/<int:round_num>', methods=['GET'])
@cross_origin()
def text_query(game_id, round_num):
    return jsonify(db.card_query(game_id, round_num))


@app.route('/<int:yearFrom>/<int:yearTo>/<string:genre>/moviesCount',methods = ['GET'])
@cross_origin()
def moviesCount(yearFrom, yearTo, genre):
    response = jsonify(db.count_movies(yearFrom, yearTo, genre))
    return response