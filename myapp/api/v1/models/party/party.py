from flask import make_response,jsonify,request
import json

partylist=[]
class Parties:
    def __init__(self,party_name=None,hq_address=None,logo_url=None):        
        self.party_name=party_name
        self.logo_url=logo_url
        self.hq_address=hq_address
        self.partylist=partylist
    
        
        #create parties
    def create_party(self):      
        for p in self.partylist:
            if p["party_name"]==self.party_name:                
                return make_response(jsonify({"status":416,"message":"party with a duplicate name exists"}))
        if self.party_name=="" and self.hq_address=="" and self.logo_url=="":           
            return make_response(jsonify({"status":400,"message":"party details not provided"}))
        if  self.logo_url=="":           
            return make_response(jsonify({"status":400,"message":"Required details not provided"}))
        if  self.hq_address=="":          
            return make_response(jsonify({"status":400,"message":"Required details not provided"}))
        if self.party_name=="":          
            return make_response(jsonify({"status":400,"message":"Required details not provided"}))      
        new={
        "party_id":len(partylist)+1,
        "party_name":self.party_name,
        "hq_address":self.hq_address,
        "logo_url":self.logo_url,
        }
        self.partylist.append(new)
              
        return  make_response(jsonify({"status code":201,"party":[new]}))

    #get all parties
    def get_parties(self):
        if len(self.partylist)==0:
            return make_response(jsonify({"status code":404,"message":"Parties list Empty"}))
        else:
            return make_response(jsonify({"status code":200,"parties":[self.partylist]}))
          
            
  

        #update parties  
    def update_party(self,party_name,party_id):       
        for party in self.partylist:
                if party["party_id"]==party_id:
                    party["party_name"]=party_name
                    return make_response(jsonify({"status":200,"Party":[party]}))
        return  make_response(jsonify({"status":404,"message":"party with id not found"}))    
              
    
    # delete political party
    def delete_party(self, party_id):
        for party in self.partylist:
            if party["party_id"]==party_id:
                self.partylist.remove(party)
                return  make_response(jsonify({"status":200,"party":[party]}))
        return make_response(jsonify({"status":404,"message":"Party with Id not found"}))
    
    
       #get one by party id   
    def get_one_party(self,party_id):
        for party in self.partylist:
            if party["party_id"]==party_id:                                   
                return  make_response(jsonify({"status":200,"party":[party]}))
         
        return make_response(jsonify({"status":404,"message":"Party with Id does not exist"}))   

    
