""" this is our running file """
from v1.views.office.office import officeblue
from v1.views.party.party import partyblue
from v2.views.candindate.candindate import BP_CANDINDATES
from v2.views.login.login import BP_USERLOGIN
from v2.views.petition.petition import BP_PETITION
from v2.views.register.signup import BP_REGISTER
from v2.views.vote.vote import BP_VOTING
from instance import app


app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(partyblue, url_prefix="/api/v1")
app.register_blueprint(officeblue, url_prefix="/api/v1")
app.register_blueprint(BP_CANDINDATES, url_prefix="/api/v2")
app.register_blueprint(BP_PETITION, url_prefix="/api/v2")
app.register_blueprint(BP_REGISTER, url_prefix="/api/v2")
app.register_blueprint(BP_VOTING, url_prefix="/api/v2")
app.register_blueprint(BP_USERLOGIN, url_prefix="/api/v2")

app.config['SECRET_KEY'] = "ijustdiditagain"



if __name__ == "__main__":
    app.run(debug=True)
