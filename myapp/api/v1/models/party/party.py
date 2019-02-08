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

    #get all parties
    def getparties(self):
        return self.partylist  

        #update parties  
    def update_party(self,party_id):
       for p in self.partylist:
              if p["partyid"]==party_id:                                              
                    self.partyname="partyname"
                    self.logourl="logourl"
                    self.hqaddress="hqaddress"                  
                    return self.partylist    
    
    # delete political party
    def deleteparty(self, party_id):
        for party in partylist:
            if party["partyid"]==party_id:
                self.partylist.remove(party)
                return self.partylist              

            return self.partylist     
    
