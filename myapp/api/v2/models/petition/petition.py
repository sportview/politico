from flask import Flask, Response, make_response, jsonify
from datetime import datetime
from instance import cur, conn, db


class Petition(db.Model):
    """" petition table columns """
    __tablename__ = 'petition'
    petition_id = db.Column(db.Integer(), primary_key=True)
    createdon = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    createdby = db.Column(db.String(50), nullable=False)
    office = db.Column(db.String(50), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    def __init__(self, createdby=None, office=None, body=None):
        self.createdon = datetime.utcnow()
        self.createdby = createdby
        self.office = office
        self.body = body

    def add_petition(self):
        """ create a new petition """
        if self.office == "":
            return make_response(jsonify({"status code":404, "message":"Required field are empty"}))
        if self.createdby == "":
            return make_response(jsonify({"status code":404, "message":"Required field are empty"}))
        if self.body == "":
            return make_response(jsonify({"status code":404, "message":"Required field are empty"}))    
        if len(self.body) <= 10:
                return make_response(jsonify({"status code":404, "message":"Required field are empty"}))
        new = {
            "createdon":self.createdon,
            "createdby":self.createdby,
            "office":self.office,
            "body":self.body
            }
        sql = "INSERT INTO petition (createdon,createdby,office,body) VALUES (%(createdon)s,%(createdby)s,%(office)s,%(body)s) RETURNING petition_id;"
        cur.execute(sql, new)
        conn.commit()
        petid = cur.fetchone()[0]
        cur.close()
        conn.close()
        new = {"petition_id":petid,
               "createdon":self.createdon,
               "createdby":self.createdby,
               "office":self.office,
               "body":self.body
                }
        return make_response(jsonify({"status Code":201,\
                                              "Petition":new,\
                                              "msg":"request successfull"\
                                              }))
    def get_petition(self):
        """ get all petitions """
        sql = "SELECT * FROM petition;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            createon, createdby, office, body, petition_id = items
            mylist = {
                "petition_id":petition_id,
                "created_on":createon,
                "created_by":createdby,
                "office":office,
                "body":body
                }
            result.append(mylist)
            return make_response(jsonify({"status code":200,\
                                        "petitions":result,\
                                        "message":"request successfull"\
                                        }))


    def get_one(self, petid):
        """get one office by id"""
        print(type(petid))
        #sql = "SELECT * FROM petition WHERE petition_id = %s;"
        data = cur.execute("""SELECT * FROM petition WHERE petition_id = {};""" .format((petid)))
        return make_response(jsonify({"Petition":data, "message":"request successfull"}))
        