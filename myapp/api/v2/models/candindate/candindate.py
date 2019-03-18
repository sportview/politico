from flask import Flask, make_response, jsonify
from instance import db, cur, conn

class Candindates(db.Model):
    __tablename__ = 'candindates'
    candindate_id = db.Column(db.Integer(), primary_key=True)
    candindate_office = db.Column(db.String(50), nullable=False)
    candindate_party = db.Column(db.String(50), nullable=False)
    candindate_name = db.Column(db.String(50), nullable=False)

    def __init__(self,  office=None, party=None, candindate=None):
        self.party = party
        self.office = office
        self.candindate = candindate

    def add_candindates(self):
        """ add new  candindate"""
        if self.office == "":
            return make_response(jsonify({"status code":404, "message":"office field are empty"}))
        if self.party == "":
            return make_response(jsonify({"status code":404, "message":"party field are empty"}))
        if self.candindate == "":
            return make_response(jsonify({"status code":404, "message":"Required field are empty"}))    
        new = {
            "office":self.office,
            "party":self.party,
            "candindate":self.candindate
        }
        sql = "INSERT INTO candindates (office,party,candindate)\
         VALUES (%(office)s,%(party)s,%(candindate)s) RETURNING candindate_id;"
        cur.execute(sql, new)
        conn.commit()
        cand_id = cur.fetchone()[0]
        cur.close()
        conn.close()
        new = {"candindate_id":cand_id,
               "candindate":self.candindate,
               "office":self.office,
               "party":self.party
               }
        return make_response(jsonify({"status Code":201,\
                                              "Candindate":new,\
                                              "msg":"request successfull"\
                                              }))
    def get_candindates(self):
        """ get all offices from the list"""
        sql = "SELECT * FROM candindates;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            office, party, candindate, candindate_id = items
            mylist = {
                "candindate_id":candindate_id,
                "candindate_name":candindate,
                "office":office,
                "party":party,
            }
            result.append(mylist)
        return make_response(jsonify({"status code":200,\
                                      "Candindates":result,\
                                      "message":"request successfull"
                                      }))
    def get_one(self, candid):
        """get one office by id"""
        print(candid)
        data = cur.execute("SELECT * FROM candindates WHERE candindate_id = '{}'".format(candid))
        return make_response(jsonify({"offices":data, "message":"request successfull"}))