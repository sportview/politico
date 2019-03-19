""" setting up the database files """
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psycopg2

app = Flask(__name__)

class ConnectDb():
    """connecting to the database docstring"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Dev:dogcat123@localhost/politico'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "ijustdiditagain"
    db = SQLAlchemy(app)

    """connecting to the database"""
    conn = psycopg2.connect(database='politico',g
                            user='postgres',
                            password='dogcat123',
                            host='localhost')
    cur = conn.cursor()
