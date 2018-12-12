class Customer:
    def setcustomerid(self,customerid):
        #customerid=customerid   #It'll give an error because without self it will be considered as local
                                 #variable and you can't use this out of method's scope.
        self.customerid=customerid
    
    def getcustomerid(self):
        return self.customerid

    def settelephoneno(self,teleno):
        self.teleno=teleno
    
    def gettelephoneno(self):
        return self.teleno

obj=Customer()
obj.setcustomerid(1001)
obj.settelephoneno(8511601021)
print('id:',obj.getcustomerid())
print('telephoneno:',obj.gettelephoneno())

