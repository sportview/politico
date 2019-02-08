from flask import Flask,Blueprint,jsonify,request,make_response
import json
from api.v1.models.Office.office import Office

officeblue=Blueprint("/office",__name__)

#add a new office
@officeblue.route('/office', methods=['POST'] )
def addoffice():
    if request.json:
        data=request.get_json()        
        office_name=data['office_name']
        office_type=data['office_type']
        newoffice=Office(office_name,office_type)  
        newoffice.addoffice()    
        return make_response(jsonify(data,{"status":200,"message":"office successfully created"}))
    else:
        return make_response(jsonify({"status":404,"message":"office not created"}))

 #get all offices from my dictionary
@officeblue.route('/office',methods=['GET'])
def get_offices(): 
    data=Office().get_offices() 
    return make_response(jsonify(data,{"status":200,"message":"officess created successfully"}))    

@officeblue.route('/office/<int:office_id>',methods=["GET"])
def get_one_office(office_id):
    if office_id=="":
        return make_response(jsonify({"status":404,"message":"Invalid office id "}))
    data=Office().get_one_office(office_id)
    return make_response(jsonify(data,{"status":200,"message":"success"}))
