partylist=[]
class Parties:
    def __init__(self,partyname=None,hqaddress=None,logourl=None):
        
        self.partyname=partyname
        self.logourl=logourl
        self.hqaddress=hqaddress
        self.partylist=partylist
    
        
        #create parties
    def createparty(self):
        party={
        "partyid":len(partylist)+1,
        "partyname":self.partyname,
        "hqaddress":self.hqaddress,
        "logourl":self.logourl,
        }
        self.partylist.append(party)
        return party
