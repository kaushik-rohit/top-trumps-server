from flask_pymongo import PyMongo, ASCENDING, DESCENDING
from app import app
from random import randint

# configure database
db_url = 'db:27017' # db for docker, localhost for local
db_name = 'ase'
app.config['MONGO_URI'] = 'mongodb://{}/{}'.format(db_url, db_name)
pymongo = PyMongo(app)
db = pymongo.db


def card_query(game_num):
    # skip attributes that are not needed in the frontend
    fields = {'_id': 0, 'genres': 0, 'release_date': 0, 'movieId':0, 'id':0}
    # set a random seed to note start from the beginning when re-enter the game
    start_pos = 0
    if game_num == 1:
        start_pos = randint(1, 1200)
    cursor = db.movies.find(projection = fields, skip = (start_pos + game_num - 1) * 20 % 1200).limit(20)
    docs = list(cursor)
    return docs


# private function, check bounds
def year_bounds():
    """
    find the lower bound and upper bound  of the year of movies
    """
    bounds = list(db.movies.aggregate([
        { "$group": {
            "_id": None,
            "lb": { "$max": "$release_date" },
            "up": { "$min": "$release_date" }
        }},
    ]))
    lb = bounds[0]['lb']
    up = bounds[0]['up']

    # select the year from the string, or integer
    if not isinstance(lb, int):
        lb = int(lb[0:4])
    if not isinstance(up, int):
        up = int(up[0:4])
    return lb, up


# private function, check all genres
def genre_all():
    """
    find distinct genres in the movies dataset
    """
    genres = db.movies.aggregate([
        {
            '$unwind': '$genres' # produce a new docs for each genre in the array
        },
        {
          '$group':{
              '_id': '$genres.name'
          }
        }
    ])
    genre_list = [elem['_id'] for elem in list(genres)]
    return genre_list


# count number of movies for displaying in login page
def count_movies(yearFrom, yearTo, genre = None):
    count = db.movies.find({'release_date':{'$gte': yearFrom, '$lte': yearTo}}).count()
    return count


# testing
if __name__ == "__main__":
    print(card_query(1))
    # print(year_bounds())
    # print(genre_all())
    # print(count_movies(1980, 2000))
