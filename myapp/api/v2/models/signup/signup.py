""" user registration """
from flask import make_response, jsonify
from instance import cur, db, conn

class Users(db.Model):
    """"user details table"""
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    other_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer(), nullable=False)
    passport_url = db.Column(db.String(50), nullable=False)
    isadmin = db.Column(db.Integer(), nullable=False)

    def __init__(self, firstname=None, lastname=None, othername=None, \
        email=None, phone_number=None, passporturl=None):
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phone_number = phone_number
        self.passporturl = passporturl
        self.isadmin = False
    def add_user(self):
        """ adding new users """
        if self.firstname == "":
            return make_response(jsonify({"status code":404, "message":"firstname field empty"}))
        if self.lastname == "":
            return make_response(jsonify({"status code":404, "message":"lastname field empty"}))
        if self.othername == "":
            return make_response(jsonify({"status code":404, "message":"Othername field empty"}))
        if self.passporturl == "":
            return make_response(jsonify({"status code":404, "message":"passporturl field empty"}))
        if self.email == "":
            return make_response(jsonify({"status code":404, "message":"Email field empty"}))
        if self.phone_number == "":
            return make_response(jsonify({"status code":404, "message":"phone number field empty"}))
        if type(self.phone_number) != int:
            return make_response(jsonify({"status code":404, "message":"phone number  invalid"}))
        new_user = {
            "first":self.firstname,
            "last":self.lastname,
            "other":self.othername,
            "email":self.email,
            "phone":self.phone_number,
            "passport":self.passporturl,
            "isadmin":self.isadmin
            }
        sql = "INSERT INTO users (firstname, lastname, othername, email, \
                                 phonenumber,passporturl, isadmin)\
               VALUES           (%(first)s, %(last)s, %(other)s, %(email)s, \
                                %(phone)s, %(passport)s, %(isadmin)s) RETURNING userid;"
        cur.execute(sql, new_user)
        conn.commit()
        userid = cur.fetchone()[0]
        cur.close()
        conn.close()
        new = {
            "user_id":userid,
            "first_name":self.firstname,
            "last_name":self.lastname,
            "other_name":self.other_name,
            "email":self.email,
            "contacts":self.phone_number,
            "passporturl":self.passporturl,
            "isadmin":self.isadmin
            }
        return make_response(jsonify({"status Code":201,\
                                      "office":new,\
                                      "msg":"request successfull"\
                                      }))

    def get_users(self):
        """ get all offices from the list"""
        sql = "SELECT * FROM users;"
        cur.execute(sql)
        data = cur.fetchall()
        result = []
        for i, items in enumerate(data):
            firstname, lastname, othername, email, phone, passport, isadmin,userid = items
            mylist = {
                "user_id":userid,
                "first_name":firstname,
                "last_name":lastname,
                "other_name":othername,
                "email":email,
                "contacts":phone,
                "passporturl":passport,
                "isadmin":isadmin
            }
            result.append(mylist)
        return make_response(jsonify({"status code":200,
                                      "users":result,
                                      "message":"request successfull"
                                      }))
    def get_one(self, usid):
        """get one office by id"""
        print(type(usid))
        data = cur.execute("SELECT * FROM users WHERE userid = userid ")
        return make_response(jsonify({"user":data, "message":"request successfull"}))
