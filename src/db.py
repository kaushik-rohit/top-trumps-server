from flask_pymongo import PyMongo, ASCENDING, DESCENDING
from app import app

# configure database
db_url = 'localhost:27017'
app.config['MONGO_URI'] = 'mongodb://{}/ase'.format(db_url)
pymongo = PyMongo(app)
db = pymongo.db


def card_query(game_id, round_num):
    fields = {'_id': 0, 'genres': 0, 'release_date': 0, 'movieId':0, 'id':0}
    # condition = {'revenue': {'$gt': 0}} # skip those movies with missing revenue
    cursor = db.movies.find(projection = fields, skip = (round_num - 1) * 20).limit(1)
    docs = list(cursor)
    print(docs[0].keys())
    return docs


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

def count_movies(yearFrom, yearTo, genre = None):
    count = db.movies.find({'release_date':{'$gte': yearFrom, '$lte': yearTo}}).count()
    return count


# testing
if __name__ == "__main__":
    print(card_query(1,1))
    # print(year_bounds())
    # print(genre_all())
    # print(count_movies(1980, 2000))