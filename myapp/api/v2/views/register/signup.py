""" registration docstring"""
from flask import  Blueprint, request
from v2.models.signup.signup import Users
from v2.views.login.login import token_required

BP_REGISTER = Blueprint("/signup", __name__)


@BP_REGISTER.route('/signup', methods=['POST'])
@token_required
def add_user():
        """add a new user"""
        if request.get_json():
                data = request.get_json()
                first_name = data['first_name']
                last_name = data['last_name']
                other_name = data['other_name']
                email = data['email']
                phone_number = data['phone_number']
                passport_url = data['passport_url']
                isadmin = data['isadmin']
                newuser = Users(first_name, last_name, other_name, email, phone_number, passport_url, isadmin)
                return newuser.add_user()

@BP_REGISTER.route('/signup', methods=['GET'])
@token_required
def get_all():
        """ get all users """
        data = Users().get_users()
        return data

@BP_REGISTER.route('/signup/<int:usid>', methods=['GET'])
@token_required
def get_one(usid):
        """ get user by id """
        data = Users().get_one(usid)
        return data
