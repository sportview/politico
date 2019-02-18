from flask import json
import os
import unittest
from api import create_app
from instance.config import Config
from api.v1.models.office import office


class  Test_Offices(unittest.TestCase):
    """test office endpoints"""

    def setUp(self):  
        self.app=create_app("testing").test_client() 
        
        self.new_office={
            "office_name":"Judiciary",
            "type":"court"
        }
    def tearDown(self):
        self.app=None



    def test_add_office(self):
        """ tests that an office was created successfully """
        response=self.app.post('api/v1/office', json=self.new_office)
    
        
        self.assertEqual(response['status'],200)
        self.assertEqual(response['message'],"office successfully created")
      
    
    def test_get_offices(self):
        """ Tests the get offices functionality"""
        response=self.office.post('api/v1/office',json=self.new_office)
        self.new_office["office_name"]="court"
        self.new_office["office_type"]="judiciary"
        response=self.office.post('api/v1/office',json=self.new_office)    
        data=response.get_json()

        self.assertEqual(data['status'],200)
        self.assertEqual(data['message'],'Request successfull')


    def test_get_one_office(self):
        self.office.post('/api/v1/office',json=self.new_office)


        response=self.office.get_one_office('api/v1/office/1')
        data=response.get_json()

        self.assertEqual(data['status'],200)
        self.assertEqual(data['message'],'request sent successfully')        
      

    if __name__ == "__main__":
        unittest.main()
        