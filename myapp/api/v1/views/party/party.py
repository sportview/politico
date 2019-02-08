from flask import Flask,Blueprint,jsonify,request,make_response
import json
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
   

