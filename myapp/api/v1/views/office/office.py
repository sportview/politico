from flask import Flask,Blueprint,jsonify,request,make_response
import json
from v1.models.office.office import Office

officeblue=Blueprint("/office",__name__)

#add a new office
@officeblue.route('/office', methods=['POST'] )
def add_office():
        if request.get_json():                
                data=request.get_json()        
                office_name=data['office_name']
                office_type=data['office_type']
                new=Office(office_name,office_type)  
                return new.add_office()
                
       
        
 #get all offices from my dictionary
@officeblue.route('/office',methods=['GET'])
def get_offices(): 
    data=Office().get_offices() 
    return data   

@officeblue.route('/office/<int:office_id>',methods=["GET"])
def get_one_office(office_id):    
    data=Office().get_one_office(office_id)
    return data
