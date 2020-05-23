from flask import jsonify, request
from flask_cors import cross_origin
from app import app
import db


@app.route('/game/<int:yearFrom>/<int:yearTo>/<string:genre>', methods=['GET'])
@cross_origin()
def text_query(yearFrom, yearTo, genre):
    return jsonify(db.card_query(yearFrom, yearTo, genre))


@app.route('/<int:yearFrom>/<int:yearTo>/<string:genre>/moviesCount',methods = ['GET'])
@cross_origin()
def moviesCount(yearFrom, yearTo, genre):
    return jsonify(db.count_movies(yearFrom, yearTo, genre))
