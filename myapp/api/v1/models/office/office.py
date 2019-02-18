from flask import Response,make_response,jsonify
type_list=["federal","legislative","state","local government"]
officelist=[]
class Office:
    def __init__(self,office_name=None,office_type=None):
        self.office_name=office_name
        self.office_type=office_type
        self.officelist=officelist
        self.type_list=type_list 

    def add_office(self):
        if self.office_name=="":
            return make_response(jsonify({"status":400,"Message":"office name required"}))
        for p in self.officelist:
            if p["office_name"]==self.office_name and p["office_type"]==self.office_type:                
                return make_response(jsonify({"status":416,"message":"office with duplicate details created"}))
        if self.office_type=="":
            return make_response(jsonify({"status":400,"Message":"office type required"}))     
        for f in self.type_list:
            if f==self.office_type:
                off_type=f
                newoffice={"office_id":len(officelist)+1,
                "office_name":self.office_name,
                "office_type":off_type}
                self.officelist.append(newoffice)
                return make_response(jsonify({"status code":201,"Office":newoffice,"message":"Office created successfully"}))            
        return make_response(jsonify({"status code":400,"message":"Office type not specified"}))

    # get all political offices
    def get_offices(self):
        if len(self.officelist)==0:
            return make_response(jsonify({"status code":404,"Offices":self.officelist,"message":"Office list empty"}))
        else:
             return make_response(jsonify({"status code":200,"Offices":self.officelist,"message":"Request successfull"}))

    #get one office
    def get_one_office(self,y):
        for off in self.officelist:
            if off["office_id"]==y:               
                return  make_response(jsonify({"status code":200,"Office":off,"message":"Request successfull"}))
        return make_response(jsonify({"status code":404,"message":"office with Id does not exist"}))
        