from flask_pymongo import PyMongo
from app import app

# configure database
db_url = 'localhost:27017'
app.config['MONGO_URI'] = 'mongodb://{}/ase'.format(db_url)
db = PyMongo(app).db

def card_query(game_id, round_num):
    fields = {'_id': 0, 'id': 1, 'revenue': 1, 'runtime': 1, 'popularity': 1, 'title': 1}
    condition = {'revenue': {'$gt': 0}} # skip those movies with missing revenue
    cursor = db.movies.find(filter = condition, projection = fields, skip = (round_num - 1) * 20).limit(20)
    docs = list(cursor)
    return docs
