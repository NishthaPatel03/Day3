class Customer:
    def setcustomerid(self,id):
        self.__customerid=id  #customerid is private variable
    
    def settelephoneno(self,teleno):
        self.__telephoneno=teleno

    def getcustomerid(self):
        return self.__customerid
    
    def gettelephoneno(self):
        return self.__telephoneno

obj=Customer()
obj.setcustomerid(1001)
obj.settelephoneno(8511601021)
print('Customer id:',obj.getcustomerid())
print('telephone no:',obj.gettelephoneno())
