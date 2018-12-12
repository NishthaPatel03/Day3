class Customer:
    counter=1000
    def __init__(self):
        Customer.counter=Customer.counter+1
        self.customerid=Customer.counter

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

    @staticmethod
    def totalcustomer():
        return Customer.counter-1000

customer1=Customer()
print('Customer id:',customer1.getcustomerid())

customer2=Customer()
print('Customer id:',customer2.getcustomerid())

print('Total customer:',Customer.totalcustomer())