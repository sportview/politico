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