officelist=[]
class Office:
    def __init__(self,office_type=None,office_name=None):
            
        
        self.office_type=office_type
        self.office_name=office_name
        self.officelist=officelist
     
    
        
        #create parties
    def addoffice(self):
        newoffice={
        "office_id":len(officelist)+1,
        "office_name":self.office_name,
        "office_type":self.office_type,        
        }
        self.officelist.append(newoffice)
        return newoffice

    # get all political offices
    def get_offices(self):
        return self.officelist 


    #get one office
    def get_one_office(self,office_id):
          
        for office in self.officelist:
        
            if office["office_id"]==office_id:                                   
                return office
        return "office not found"   
 