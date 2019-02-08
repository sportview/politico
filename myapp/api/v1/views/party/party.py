from flask import Flask,Blueprint,jsonify,request,make_response
import json

from myapp.api.v1.models.party.party import Parties

from api.v1.models.party.party import Parties

partyblue=Blueprint("/parties",__name__)

#add a political party
@partyblue.route('/parties', methods=['POST'] )
def addparty():
    if request.json:
        data=request.get_json()
        name=data['partyname']
        address=data['hqaddress']
        urllogo=data['logourl']
        newparty=Parties(name,address,urllogo)  
        newparty.createparty()      
        return make_response(jsonify(newparty,{"status":201,"Message":"new party successfully created"}))
    return make_response(jsonify(newparty,{"status":404,"Message":"party not created"}))
   
  #get all parties from my dictionary
@partyblue.route('/parties',methods=['GET'])
def getparties(): 
    plist=Parties().getparties()
    return make_response(jsonify(plist,{"status":200,"message":"success"})) 

@partyblue.route('/parties/<int:party_id>', methods=['PATCH'] )
def update_party_name(party_id):
    data=request.get_json()
    name=data['partyname']
    address=data['hqaddress']
    urllogo=data['logourl']
    updated_party=Parties().update_party(name,address,urllogo)

    return make_response(jsonify(updated_party,{"status":200,"message":"success"}))     