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
