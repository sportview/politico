from flask import make_response, jsonify
from instance import db, cur, conn
from basemodel.base import BaseDb


class Parties(db.Model):
    """political parties tables format"""
    __tablename__ = 'party'
    party_id = db.Column(db.Integer(), primary_key=True)    
    party_name = db.Column(db.String(50), nullable=False)
    hq_address = db.Column(db.String(50), nullable=False)
    logo_url = db.Column(db.String(50), nullable=False)

    def __init__(self, party_name=None, hq_address=None, logo_url=None):        
        self.party_name = party_name
        self.logo_url = logo_url
        self.hq_address = hq_address

    def create_party(self):
        """create new party """
        if BaseDb().check_exist('party', 'pname', self.party_name) == True:
            return make_response(jsonify({"msg":"party exists"}), 404)
        if self.party_name == "" and self.hq_address == "" and self.logo_url == "":
            return make_response(jsonify({"status":400, 
                                          "message":"party details not provided"
                                          }))
        if  self.logo_url == "":
            return make_response(jsonify({"status":400, "message":"Required details not provided"}))
        if  self.hq_address == "":
            return make_response(jsonify({"status":400, "message":"Required details not provided"}))
        if self.party_name == "":
            return make_response(jsonify({"status":400, "message":"Required details not provided"}))
        new = {"party_name":self.party_name,
               "hq_address":self.hq_address,
               "logo_url":self.logo_url}
        sql = "INSERT INTO party (pname,hqaddress,logourl) VALUES \
                                  (%(party_name)s, %(hq_address)s, \
                                  %(logo_url)s) RETURNING party_id;"
        cur.execute(sql, new)
        conn.commit()
        party_id = cur.fetchone()[0]        
        #cur.close()
        #conn.close()
        newparty = {"party_id":party_id,\
               "party_name":self.party_name,\
               "hq_address":self.hq_address,\
               "logo_url":self.logo_url}
        return  make_response(jsonify({"status code":201,
                                       "party":newparty, \
                                       "msg":"party created "}))

    def get_parties(self):
        """get parties docstring"""
        sql = "SELECT * FROM party;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            pname, hqaddress, logourl, party_id = items
            mylist = {
                "party_id":party_id,
                "party_name":pname,
                "hq_address":hqaddress,
                "logourl":logourl
            }
            result.append(mylist)
            return make_response(jsonify({"status code":200,\
                                      "offices":result,\
                                      "message":"request successfull"}))

    def update_party(self, party_name, hq_address, logo_url, item_id):
        """ update party details """
        if BaseDb().check_exist('party', 'party_id', item_id) == False:
            return make_response(jsonify({'status code':400, 'Message':'party does not exist'}))             
        if BaseDb().check_exist('party', 'pname', party_name) == True:
            return make_response(jsonify({'status code':400, 'msg':'Party with an existing name exists'}))
        BaseDb().update_item('party', 'pname', party_name, 'hqaddress', hq_address, 'logourl', logo_url, 'party_id', item_id)
        return make_response(jsonify({'Status':200, 'Message':'Party updated successfully'}))
          

    def delete_party(self, party_id):
        """delete political party"""
        if BaseDb().delete_item('party', 'party_id', party_id) == False:
            return make_response(jsonify({"status code":404, "msg":"party does not exist"}))
        query = "DELETE FROM party WHERE party_id = {}".format(party_id)
        cur.execute(query)
        cur.close()
        return make_response(jsonify({"status code":200,\
                                      "message":"party deleted successfully"}))

    def get_one_party(self, party_id):
        """get one by party id"""
        if BaseDb().check_exist('party', 'party_id', party_id) == False:
            return make_response(jsonify({"status code":404, "msg":"party does not exist"}))
        query = "SELECT * FROM party WHERE party_id = {}".format(party_id)
        cur.execute(query)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            pname, hqaddress, logourl, party_id = items
            mylist = {
                "party_id":party_id,
                "party_name":pname,
                "hq_address":hqaddress,
                "logourl":logourl
            }
            result.append(mylist)
            return make_response(jsonify({"status code":200,\
                                      "party":result,\
                                      "message":"Request processed successfull"}))
