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
        else:
                return make_response(jsonify({"Status code":400,"message":"invalid data format"}))        
 #get all offices from my dictionary
@officeblue.route('/office',methods=['GET'])
def get_offices():
        if request.get_json():
                data=Office().get_offices()
                return data
        else:
                return make_response(jsonify({"status code":400,"message":"Invalid data format"}))        
@officeblue.route('/office/<int:y>',methods=["GET"])
def get_one_office(y):
        if request.get_json():
                data=Office().get_one_office(y)
                return data
        else:
                return make_response(jsonify({"status code":400,"message":"Invalid data format"}))
                