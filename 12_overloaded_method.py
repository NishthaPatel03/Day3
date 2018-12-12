class printDetails:
    def printHeader(self,c='*',no=1):
        print(c*no)

obj=printDetails()
obj.printHeader('#',10)
obj.printHeader('Report')
obj.printHeader('#',10)
