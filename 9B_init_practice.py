class Customer:
    
    def __init__(self,id,name,phoneno):
        self.customerid=id
        self.customername=name
        self.telephoneno=phoneno

    def setcustomerid(self,id):
        self.customerid=id  
    
    def settelephoneno(self,teleno):
        self.telephoneno=teleno

    def setcustomername(self,name):
        self.customername=name 

    def getcustomername(self):
        return self.customername
    
    def getcustomerid(self):
        return self.customerid
    
    def gettelephoneno(self):
        return self.telephoneno

    def validatecustomername(self):
        if(len(self.customername)>=3 and len(self.customername)<=20):
            return True
        else:
            return False


telephone=[7016650626,8511601021,8200277672]
obj=Customer(1001,'Nishtha',telephone)
if(obj.validatecustomername()):  
    print('Customer id:',obj.getcustomerid())
    print('Customer name:',obj.getcustomername())
    print('telephone no:',obj.gettelephoneno())
else:
    print('Name must be between 3 to 20 characters')