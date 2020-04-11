from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
# configure database
url = 'localhost:27017'
app.config['MONGO_URI'] = 'mongodb://{}/ase'.format(url)
db = PyMongo(app).db

@app.route('/game/<int:game_id>', methods=['GET'])
def text_query(game_id):
    round_num = int(request.form['round_num']) # put round number in get request body
    fields = {'_id': 0, 'id': 1, 'revenue': 1, 'runtime': 1, 'popularity': 1, 'title': 1}
    condition = {'revenue': {'$gt': 0}} # skip those movies with missing revenue
    cursor = db.movies.find(filter = condition, projection = fields, skip = (round_num - 1) * 20).limit(20)
    docs = list(cursor)
    return jsonify(docs)


if __name__ == '__main__':
    host_addr = 'localhost'
    app.run(host= host_addr, port=5001, debug=True)
