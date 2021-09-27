from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
    
    print('Before Everything!')

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'UwU'

    
    from .models import Note
    
    create_database(app)
    return app

def create_database(app):

    print('Start create_database!')

    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database name = ' + DB_NAME)
        

