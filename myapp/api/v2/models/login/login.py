"""
 The login model route
 """
from flask import Response, make_response, jsonify
from api import config, db

class Login(db.Model):
    """login  details"""

    username = db.Column(db.String(50), nullable=False)
    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password
    
    def user_login(self):
        """ login function """
        
        return make_response(jsonify({"logged in"}))
        