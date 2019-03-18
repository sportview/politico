""" Petition docstring """
from flask import Blueprint, request
from v2.views.login.login import token_required
from v2.models.petition.petition import Petition

BP_PETITION = Blueprint("/petition", __name__)

""" add a new office """
@BP_PETITION.route('/petition', methods=['POST'])
@token_required
def create_petition():
        """create petition"""
        if request.get_json():
                data = request.get_json()
                createdby = data['createdby']
                office = data['office']
                body = data['body']
                new = Petition(createdby, office, body)
        return new.add_petition()

@BP_PETITION.route('/petition', methods=['GET'])
@token_required
def get_all():
        """get all offices from my dictionary"""
        data = Petition().get_petition()
        return data

@BP_PETITION.route('/petition/<int:petid>', methods=["GET"])
@token_required
def get_one(petid):
        """get petitions by id"""
        data = Petition().get_one(petid)
        return data
