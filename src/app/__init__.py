from flask import Flask

app = Flask(__name__)

from app import routes

# from the following website 
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world