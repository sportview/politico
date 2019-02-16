'''Creating app for different environments'''
import os

from flask import Flask, Blueprint
from instance.config import app_config
from api.v1.views.party.party import Parties
from api.v1.views.office.office import Office
from api.v1.views.party.party import partyblue
from api.v1.views.office.office import officeblue

def create_app(config_name):    
    "instattiate the flask app"
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])  

    # register blueprints
    app.register_blueprint(partyblue)
    app.register_blueprint(officeblue)    
    return app
   