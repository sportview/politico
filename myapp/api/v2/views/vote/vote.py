""" lets vote it is our right"""
from flask import Blueprint, request
from v2.models.vote.vote import Vote
from v2.views.login.login import token_required

BP_VOTING = Blueprint("/vote", __name__)


@BP_VOTING.route('/vote', methods=['POST'])
@token_required
def vote():
        """LETS VOTE NOW"""
        if request.get_json():
                data = request.get_json()
                createdby = data['createdby']
                office = data['office']
                candindate = data['candindate']
                haki = Vote(createdby, office, candindate)
                return haki.voted()

@BP_VOTING.route('/vote', methods=['GET'])
@token_required
def get_all():
        """ get all votes """
        data = Vote().get_votes()
        return data

@BP_VOTING.route('/vote/<int:voteid>', methods=["GET"])
@token_required
def get_one(voteid):
        """ get votes by id """
        data = Vote().get_one(voteid)
        return data
