from flask import Flask,Blueprint,jsonify,request,make_response
import json
from v1.models.party.party import Parties


partyblue=Blueprint("/parties",__name__)

#add a political party
@partyblue.route('/parties', methods=['POST'] )
def add_party():
        if request.get_json():
                data=request.get_json()          
                name=data['party_name']
                address=data['hq_address']
                logo=data['logo_url']
                new_party=Parties(name,address,logo)                          
              
                return  new_party.create_party()
          #get all parties from my dictionary
@partyblue.route('/parties',methods=['GET'])
def get_parties():
        if request.get_json():
                data=Parties().get_parties()
                return data                                  
      
@partyblue.route('/parties/<int:party_id>', methods=['PATCH'] )
def update_party_name(party_id):
        if request.get_json():
                data=request.get_json()                             
                party_name=data["party_name"]
                response=Parties().update_party(party_name,party_id)
                return response
#Delete political party
@partyblue.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_party(party_id):
        if request.get_json():
                data=Parties().delete_party(party_id)   
                return data

#get one specific party
@partyblue.route('/parties/<int:party_id>',methods=["GET"])
def get_one_party(party_id):
    response=Parties().get_one_party(party_id)
    return response