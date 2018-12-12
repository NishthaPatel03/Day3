#Assignment 17

"""
For association, class diagram is given
"""

class PrintDetails:
    def printheader(self,c,no=1):
        print(c*no)

class PurchaseBill:
    def __init__(self,bid,billamount):
        self.__billid = bid
        self.__billamount = billamount
    def getbillid(self):
        return self.__billid
    def getbillamount(self):
        return self.__billamount
    def calculatebill(self, mode, processcharge):
        if(mode == "credit"):
            self.__billamount = self.__billamount + (self.__billamount * processcharge / 100)
    def displaybill(self):
        obj = PrintDetails()
        obj.printheader("-",80)
        obj.printheader("SHOPIING SITE")
        obj.printheader("-",80)
        print("Bill Id : ",self.__billid)
        print("Final amount : ",self.__billamount)
        obj.printheader("-",80)
        obj.printheader(" Thank you !!!")
        obj.printheader("-",80)
objpur = PurchaseBill(101,1055.0)
objpur.calculatebill("credit",10.5)
objpur.displaybill()

"""
--------------------------------------------------------------------------------
SHOPIING SITE
--------------------------------------------------------------------------------
Bill Id :  101
Final amount :  1165.775
--------------------------------------------------------------------------------
 Thank you !!!
--------------------------------------------------------------------------------
"""




        