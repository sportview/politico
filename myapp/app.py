from flask import Flask,jsonify,make_response,request
app=Flask(__name__)
from api.v1.views.party.party import partyblue
#from api.v1.views.Office.office import officeblue
app.register_blueprint(partyblue,url_prefix="/api/v1")
#app.register_blueprint(officeblue,url_prefix="/api/v1")
@app.route("/all")
def all_routes():
    routes=[]
    for route in app.url_map.iter_rules():
        routes.append(str(route))


    return make_response(jsonify(routes), 200)


    
if __name__ == "__main__":
    app.run(debug=True)