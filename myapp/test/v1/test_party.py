from api.config import create_app
import unittest
from flask import Flask, jsonify,json
from api.v1.models.party.party import Parties



class Test_Parties(unittest.TestCase):
    """ Tests for all parties endpoints """

    def setUp(self):   
        self.app=create_app("testing").test_client() 

        self.new_party = {
            "party_name": "ODM",           
            "hq_address": "yawezekana",
            "logo_url": "www.logo.url"
        }

  

    # tests POST method creating parties
    def test_add_party(self):
        """ Tests for creating parties """
        response = self.app.post('/api/v1/parties', json=self.new_party)
        data = response.get_json()
        self.assertEqual(data['status code'], 201)
        self.assertEqual(data['message'], 'Party successfully created')


   
    def test_get_parties(self):
        """ Tests when get request made to api/v1/parties """
        response = self.app.post('/api/v1/parties', json=self.new_party)     
      
        self.new_party['name'] = 'Other Other name'
        response = self.app.post('/api/v1/parties', json=self.new_party)

        response = self.app.get('/api/v1/parties')
        data = response.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], "Request successfull")
  

    

    # tests for GET a specific party
    def test_get_one_party(self):
        """ test to get a specific party by id api/v1/parties/<int:party_id> """

        self.app.post('/api/v1/parties', json=self.new_party)

        response = self.app.get('/api/v1/parties/1')
        data = response.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Request successfully')
      
 

    # tests for DELETE party
    def test_delete_party(self):
        """ Tests delete by passing party id on url /parties/<int:id> """

        self.app.post('/api/v1/parties', json=self.new_party)
        response = self.app.delete('/api/v1/parties/1')
        data = response.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'party successfully deleted')
       

  

    # tests for PATCH party
    def test_update_party(self):
        """ Tests PATCH in Parties /parties/<int:party_id>"""

        self.app.post('/api/v1/parties', json=self.new_party)

        response = self.app.patch('/api/v1/parties/1')
        
        data = response.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'party successfully updated')
        

   