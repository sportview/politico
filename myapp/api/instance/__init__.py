""" setting up the database files """
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psycopg2

app = Flask(__name__)
"""app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DEV:dogcat123@LOCALHOST/politico'"""
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = "ijustdiditagain"
db = SQLAlchemy(app)

"""connecting to the database"""
conn = psycopg2.connect(database='politico',
                        user='postgres',
                        password='dogcat123',
                        host='localhost')
#print("connection successful database are you sure")
cur = conn.cursor()
