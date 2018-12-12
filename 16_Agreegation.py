#Assignment 16

"""
for agreegation, class diagram is given
"""

class Address:
    def __init__(self, addline, city, state, zip):
        self.__addline = addline
        self.__city = city
        self.__state = state
        self.__zip = zip
    def setaddline(self,addline):
        self.__addline = addline
    def getaddline(self):
        return self.__addline
    def setcity(self,city):
        self.__city = city
    def getcity(self):
        return self.__city
    def setstate(self,state):
        self.__state=state
    def getstate(self):
        return self.__state
    def setzip(self,zip):
        self.__zip = zip
    def getzip(self):
        return self.__zip
    
class Customer:
    def __init__(self,cid,address):
        self.__customerid = cid
        self.__address = address

    def getcustomerid(self):
        return self.__customerid
    def getaddress(self):
        return self.__address

address = Address("Nishtha","38 Megh Milap Vatika","Surat","395005")
customer = Customer(1001,address)

print("Id :",customer.getcustomerid())
add = customer.getaddress()
print("Address :")
print(add.getaddline())
print(add.getcity())
print(add.getstate())
print(add.getzip())

"""
Id : 1001
Address :
Bhargav Rathod
29-30 A Nimisha
Nadiad
387001
"""