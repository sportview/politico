from .base_test import Base



class TestParties(Base):
    """ Tests for all parties endpoints """

    def setUp(self):   

        self.new_party = {
            "party_name": "ODM",           
            "hq_address": "yawezekana",
            "logo_url": "url"
        }

  

    # tests POST method creating parties
    def test_add_party(self):
        """ Tests for creating parties """
        response = self.client.post('/api/v1/parties', json=self.new_party)
        data = response.get_json()
        self.assertEqual(data['status'], 201)
        self.assertEqual(data['message'], 'Party successfully created')


   
    def test_get_parties(self):
        """ Tests when get request made to api/v1/parties """

        res = self.client.post('/api/v1/parties', json=self.new_party)
        self.new_party['name'] = 'Other name'
        res = self.client.post('/api/v1/parties', json=self.new_party)
        self.new_party['name'] = 'Other Other name'
        res = self.client.post('/api/v1/parties', json=self.new_party)

        res = self.client.get('/api/v1/parties')
        data = res.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], "Request successfull")
  

    

    # tests for GET a specific party
    def test_get_one_party(self):
        """ test to get a specific party by id /parties/<int:party_id> """

        self.client.post('/api/v1/parties', json=self.new_party)

        res = self.client.get('/api/v1/parties/1')
        data = res.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'Request successfully')
      
 

    # tests for DELETE party
    def test_delete_party(self):
        """ Tests delete by passing party id on url /parties/<int:id> """

        self.client.post('/api/v1/parties', json=self.new_party)

        res = self.client.delete('/api/v1/parties/1')
        data = res.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'party successfully deleted')
       

  

    # tests for PATCH party
    def test_update_party(self):
        """ Tests PATCH in Parties /parties/<int:party_id>"""

        self.client.post('/api/v1/parties', json=self.new_party)

        res = self.client.patch('/api/v1/parties/1/Rainbow')
        data = res.get_json()

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'party successfully updated')
          