from flask import make_response, jsonify
from instance import db, cur, conn
from basemodel.base import BaseDb
type_list = ["federal", "legislative", "state", "local government"]
class Office(db.Model):
    __tablename__ = 'office'
    office_id = db.Column('office_id', db.Integer, primary_key=True)
    office_name = db.Column('office_name', db.String(50), unique=True, nullable=False)
    office_type = db.Column('office_type', db.String(50), unique=True, nullable=False)

    def __init__(self, office_name=None, office_type=None):
        self.office_name = office_name
        self.office_type = office_type
        self.type_list = type_list
    def add_office(self):
        """ add a new office"""
        if self.office_name == "" and self.office_type == "":
            return make_response(jsonify({"status":400,
                                          "message":"Office details not provided"}))
        if  self.office_name == "":
            return make_response(jsonify({"status":400,
                                          "message":"Required details not provided"
                                          }))
        if self.office_type == "":
            return make_response(jsonify({"status":400, "Message":"office type required"}))     
        for f in self.type_list:
            if f == self.office_type:
                off_type = f
                newoffice = {
                   "offname":self.office_name,
                   "offtype":off_type
                   }
                sql = "INSERT INTO office (office_name,office_type) VALUES (%(offname)s,%(offtype)s) RETURNING office_id;"
                cur.execute(sql, newoffice)
                conn.commit()
                office_id = cur.fetchone()[0]
                cur.close()
                conn.close()
                new = {
                    "office_id":office_id,
                    "office_name":self.office_name,
                    "office_type":self.office_type
                }
                return make_response(jsonify({"status Code":201,
                                              "office":new,
                                              "msg":"request successfull"}))
        return make_response(jsonify({"status code":400,
                                      "message":"Office type not specified"\
                                    }))
    def get_offices(self):
        """ get all offices from the list"""
        sql = "SELECT * FROM office;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            office_id, office_name, office_type = items
            mylist = {
                "office_id":office_id,
                "office_name":office_name,
                "office_type":office_type
            }
            result.append(mylist)
        return make_response(jsonify({"status code":200,
                                      "offices":result,
                                      "message":"request successfull"
                                      }))
    def get_one_office(self, offid):
        """get one office by id"""
        if BaseDb().check_exist('office', 'office_id', offid) == False:
            return make_response(jsonify({"msg":"office does not exist"}), 404)
        query = "SELECT * FROM office WHERE office_id = {}".format(offid)
        cur.execute(query)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            office_id, office_name, office_type = items
            mylist = {
                "office_id":office_id,
                "office_name":office_name,
                "office_type":office_type
            }
            result.append(mylist)
        return make_response(jsonify({"status code":200,
                                      "offices":result,
                                      "message":"request successfull"
                                      }))
