""" office view docstring"""
from flask import Blueprint, request
from v1.models.office.office import Office
from v2.views.login.login import token_required

officeblue = Blueprint("/office", __name__)

#add a new office
@officeblue.route('/office', methods=['POST'] )
@token_required
def add_office():
        """ create a new office """
        if request.get_json():
                data = request.get_json()
                office_name = data['office_name']
                office_type = data['office_type']
                new = Office(office_name, office_type)
                return new.add_office()

@officeblue.route('/office', methods=['GET'])
@token_required
def get_offices():

        data = Office().get_offices()
        return data

@officeblue.route('/office/<int:offid>', methods=["GET"])
#@token_required
def get_one_office(offid):
        """ delete offices by id """
        data = Office().get_one_office(offid)
        return data
