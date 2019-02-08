from flask import Flask,jsonify,make_response,request
app=Flask(__name__)

from myapp.api.v1.views.party.party import partyblue
#from api.v1.views.Office.office import officeblue
app.register_blueprint(partyblue,url_prefix="/api/v1")
#app.register_blueprint(officeblue,url_prefix="/api/v1")



if __name__ == "__main__":
    app.run(debu=True)