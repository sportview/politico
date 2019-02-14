from flask import Response,make_response,jsonify
officelist=[]
class Office:
    def __init__(self,office_type=None,office_name=None):           
        
        self.office_type=office_type
        self.office_name=office_name
        self.officelist=officelist
     
    
    def add_office(self): 
        for p in self.officelist:
            if p["office_name"]==self.office_name:
                return make_response(jsonify({"status":416,"message":"Office with a duplicate name exists"}))
        if self.office_name=="" and self.office_type=="":           
            return make_response(jsonify({"status":400,"message":"Office details not provided"}))
        if  self.office_type=="":           
            return make_response(jsonify({"status":400,"message":"Required details not provided"}))
        if  self.office_name=="":          
            return make_response(jsonify({"status":400,"message":"Required details not provided"}))
       
        newoffice={
        "office_id":len(officelist)+1,
        "office_name":self.office_name,
        "office_type":self.office_type,        
        }
        self.officelist.append(newoffice)
        return make_response(jsonify({"status code":201,"Office":[newoffice]}))

    # get all political offices
    def get_offices(self):
        if len(self.officelist)==0:
            return make_response(jsonify({"status code":404,"Offices":[self.officelist]}))
        else:
             return make_response(jsonify({"status code":200,"Offices":[self.officelist]}))
        


    #get one office
    def get_one_office(self,office_id):          
        for office in self.officelist:
            if office["office_id"]==office_id:                                   
                return  make_response(jsonify({"status code":200,"Office":[office]}))
         
        return make_response(jsonify({"status code":404,"message":"office with Id does not exist"}))   
