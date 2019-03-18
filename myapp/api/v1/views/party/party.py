from flask import Blueprint, request, make_response, jsonify
from v1.models.party.party import Parties
from v2.views.login.login import token_required


partyblue = Blueprint("/parties", __name__)

#add a political party
@partyblue.route('/parties', methods=['POST'])
#@token_required
def add_party():
        """ create party docstring"""
        if request.get_json():
                data = request.get_json()          
                name = data['party_name']
                address = data['hq_address']
                logo = data['logo_url']
                new_party = Parties(name, address, logo)
                return  new_party.create_party()
          #get all parties from my dictionary
@partyblue.route('/parties', methods=['GET'])
@token_required
def get_parties():
        """ get parties docstring"""
        if request.get_json():
                data = Parties().get_parties()
                return data
@partyblue.route('/parties/<int:item_id>', methods=['PATCH'])
#@token_required
def update_party_name(item_id):
        """update parties docstring"""
        if request.get_json():
                data = request.get_json()
                if data['party_name'] == "":
                        return make_response(jsonify({"Status code":400, "message":"party name cannot be empty"}))
                if data['hq_address'] == "":
                        return make_response(jsonify({"Status code":400, "message":"hq address cannot be empty"}))
                if data['logo_url'] == "":
                        return make_response(jsonify({"Status code":400, "message":"logo url cannot be empty"}))        
                party_name = data["party_name"]
                hq_address = data["hq_address"]
                logo_url = data["logo_url"]
                response = Parties().update_party(party_name, hq_address, logo_url, item_id)
                return response
#Delete political party
@partyblue.route('/parties/<int:party_id>', methods=['DELETE'])
#@token_required
def delete_party(party_id):
        """delete party doctsring"""
        if request.get_json():
                data = Parties().delete_party(party_id)   
                return data

#get one specific party
@partyblue.route('/parties/<int:party_id>', methods=["GET"])
#@token_required
def get_one_party(party_id):
        """ get one party docstring"""
        response = Parties().get_one_party(party_id)
        return response
