""" the login module """
from functools import wraps
from flask import  Blueprint, jsonify, request, make_response
import jwt
from instance import app
import datetime


app.config['SECRET_KEY'] = 'ididitagain'
BP_USERLOGIN = Blueprint("/login", __name__)

#add a new office
@BP_USERLOGIN.route('/login', methods=['POST'] )
def login():
    """This is the login docstring"""
    if request.get_json():
        data = request.get_json()
        if data and  data['password'] == 1234:
                payload = {'user':data['username'], 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}
                token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                return make_response(jsonify({"message":"login successful", 'token':token.decode('UTF-8')}))
    return make_response(jsonify('could not verify', 401, {"message":"login required"}))

def token_required(f):
        """ token required docstring"""
        @wraps(f)
        def decorated(*args, **kwargs):
                token = request.args.get('token')
                if not token:
                        return make_response(jsonify({'message':'Token missing'}))

                try:
                        data = jwt.decode(token, app.config['SECRET_KEY'])
                except:
                        return make_response(jsonify({'message':'Token invalid'}))
                return f(*args, **kwargs)
        return decorated
