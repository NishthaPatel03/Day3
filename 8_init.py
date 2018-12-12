#This implement does not matches specifications.
#We need parametarized init(9_init).

class Customer:
    
    def __init__(self):
        self.customerid=1001
        self.customername=None
        self.telephoneno=[]

    def setcustomerid(self,id):
        self.customerid=id  #customerid is private variable
    
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

obj=Customer()
print('Customer id:',obj.getcustomerid())
print('Customer name:',obj.getcustomername())
print('telephone no:',obj.gettelephoneno())