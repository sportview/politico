""" Voting models """
from flask import Response, make_response, jsonify
from instance import cur, db, conn
from datetime import datetime


class Vote(db.Model):
    """ voting table layout """
    __tablename__ = 'vote'
    vote_id = db.Column(db.Integer(),primary_key=True)
    createdon = db.Column(db.DateTime(), default=datetime.utcnow)
    createdby = db.Column(db.String(50), unique=True)
    office = db.Column(db.String(50), unique=True)
    candindate = db.Column(db.String(50), unique=True)
    def __init__(self, createdby=None, office=None, candidate=None):
        self.createdon = datetime.utcnow()
        self.createdby = createdby
        self.office = office
        self.candidate = candidate

    def voted(self):
        """ haki yako ni kupiga kura"""
        if self.createdby == "":
            return make_response(jsonify({"status code":404, "message":"createdby field empty"}))
        if self.office == "":
            return make_response(jsonify({"status code":404, "message":"office field empty"}))
        if self.candidate == "":
            return make_response(jsonify({"status code":404, "message":"candidate field empty"}))    
        myvote = {
            "createdon":self.createdon,
            "createdby":self.createdby,
            "office":self.office,
            "candidate":self.candidate
            }
        sql = "INSERT INTO vote (createdon, createdby, office, candindate)\
             VALUES (%(createdon)s, %(createdby)s, %(office)s, %(candidate)s) RETURNING vote_id;"
        cur.execute(sql, myvote)
        conn.commit()
        vote_id = cur.fetchone()[0]
        cur.close()
        conn.close()
        new = {"vote_id":vote_id,
               "createdon":self.createdon,
               "createdby":self.createdby,
               "office":self.office,
               "candindate":self.candidate\
            }
        return make_response(jsonify({"status Code":201,\
                                      "office":new,
                                      "msg":"request successfull"
                                      }))
    def get_votes(self):
        """ get all votes list"""
        sql = "SELECT * FROM vote;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            createdon, createdby, office, candindate, vote_id = items
            mylist = {
                "vote_id":vote_id,
                "createdon":createdon,
                "createdby":createdby,
                "office":office,
                "candindate":candindate
            }
            result.append(mylist)
        return make_response(jsonify({"status code":200,
                                      "offices":result,
                                      "message":"request successfull"
                                      }))
    def get_one(self, voteid):
        """get one office by id"""
        print(voteid)
        data = cur.execute("SELECT * FROM vote WHERE vote_id = '{}'".format(voteid))
        return make_response(jsonify({"offices":data, "message":"request successfull"}))
