from flask import Blueprint, request
from v2.models.candindate.candindate import Candindates
from v2.views.login.login import token_required

BP_CANDINDATES = Blueprint("/candindates", __name__)

#add a new candindate
@BP_CANDINDATES.route('/candindates', methods=['POST'])
@token_required
def express():
        """ register as a candindate """
        if request.get_json():
                data = request.get_json()
                office = data['office_name']
                party = data['party_name']
                candindate_name = data['candindate_name']
                new_candindate = Candindates(office, party, candindate_name)                
        return new_candindate.add_candindates()

@BP_CANDINDATES.route('/candindates', methods=['GET'])
@token_required
def get_all_candindates():
        """get candindates"""
        data = Candindates().get_candindates()
        return data

@BP_CANDINDATES.route('/candindates/<int:candid>', methods=['GET'])
@token_required
def get_one_candindate(candid):
        """get candindates"""
        data = Candindates().get_one(candid)
        return data
        