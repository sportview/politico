from flask import Flask,jsonify,make_response,request
import os
from v1.views.party.party import partyblue
from v1.views.office.office import officeblue
from v1.views.office.office import officeblue
from v1.views.party.party import partyblue
       

app= Flask(__name__)


#app=create_app(os.getenv('app_config') or 'develop')

app.config['JSON_SORT_KEYS']=False
app.register_blueprint(partyblue,url_prefix="/api/v1")
app.register_blueprint(officeblue,url_prefix="/api/v1")






    
if __name__ == "__main__":
    app.run(debug=True)