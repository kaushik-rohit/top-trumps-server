from flask import Flask

app = Flask(__name__) # instance later can be imported

from app import routes

# from the following website 
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# about regular package: https://docs.python.org/3/reference/import.html#regular-packages 