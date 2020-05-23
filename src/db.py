from flask_pymongo import PyMongo, ASCENDING, DESCENDING
from app import app
import random 
import os

# if in container return True
SECRET_KEY = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
print("AM_I_IN_A_DOCKER_CONTAINER======={}========".format(SECRET_KEY))
db_url = 'localhost:27017' # db for docker, localhost for local
if SECRET_KEY:
    db_url = 'db:27017' 

# configure database
db_name = 'ase'
app.config['MONGO_URI'] = 'mongodb://{}/{}'.format(db_url, db_name)
pymongo = PyMongo(app)
db = pymongo.db


def card_query(yearFrom = None, yearTo = None, genre = None):
    # skip attributes that are not needed in the frontend
    filter = {'release_date':{'$gte': yearFrom, '$lte': yearTo}, 'genres.name': genre.title()}
    if genre == 'all':
        filter = {'release_date':{'$gte': yearFrom, '$lte': yearTo}}
    # set a random seed to the beginning of the game
    # start_pos = randint(1, 1500)
    fields = {'_id': 0, 'genres': 0, 'release_date': 0, 'movieId':0, 'id':0}
    cursor = db.movies.find(filter = filter, projection = fields)
    docs = list(cursor)
    # print(docs)
    res = []
    # sample 20 id and fecth
    if len(docs) >= 20:
        res = random.sample(docs, k = 20)
        random.shuffle(res)
    # shuffle the objects in the list
    return res


# private function, check bounds
def year_bounds():
    """
    find the lower bound and upper bound  of the year of movies
    """
    bounds = list(db.movies.aggregate([
        { "$group": {
            "_id": None,
            "lb": { "$min": "$release_date" },
            "up": { "$max": "$release_date" }
        }},
    ]))
    lb = bounds[0]['lb']
    up = bounds[0]['up']
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
def count_movies(yearFrom, yearTo, genre = 'all'):
    if genre == 'all':
        count = db.movies.find({'release_date':{'$gte': yearFrom, '$lte': yearTo}}).count()
    else:
        # title() convert the first word into Uppercase
        count = db.movies.find({'release_date':{'$gte': yearFrom, '$lte': yearTo}, 'genres.name': genre.title()}).count()
    return count


# testing
if __name__ == "__main__":
    # print(card_query(1900, 2000, 'all'))
    # print(year_bounds())
    # print(genre_all())
    # print(count_movies(1893, 3000, 'Adventure'))
