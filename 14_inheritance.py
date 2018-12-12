#Assignment 14

class Customer:
    def setcustomerid(self,cid):
        self.__customerid = cid
    def setcustomername(self,name):
        self.__customername = name
    def getcustomerid(self):
        return self.__customerid
    def getcustomername(self):
        return self.__customername
    
class RegularCustomer(Customer):
    def setdiscount(self,dis):
        self.__discount = dis
    def getdiscount(self):
        return self.__discount

class PrivilegedCustomer(Customer):
    def setmemcardtype(self,card):
        self.__memcardtype = card
    def getmemcardtype(self):
        return self.__memcardtype

r = RegularCustomer()
r.setcustomerid(1001)
r.setcustomername("Nishtha")
r.setdiscount(10.0)

print("Regular Customer Details:")
print("Id : ",r.getcustomerid())
print("Name : ",r.getcustomername())
print("Discount : ",r.getdiscount())
print('*'*10)

p = PrivilegedCustomer()
p.setcustomerid(1002)
p.setcustomername("Patel")
p.setmemcardtype("Gold")

print("Regular Customer Details:")
print("Id : ",p.getcustomerid())
print("Name : ",p.getcustomername())
print("Discount : ",p.getmemcardtype())
print('*'*10)




