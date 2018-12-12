#Asignment 15

#QUE 2

class Base:
    def __init__(self, v):
        self.basevar = v
        self.var = 0
        print("parent init invoked")

class Derived(Base):
    def __init__(self,v):
        super().__init__(v)
        self.dervar = v
        self.var = 0
        print("Derived init invoked")
    def display(self):
        print("Base class var : ",self.basevar)
        print("Derived class var : ",self.dervar)
    def useofsuper(self):
        self.var = 15
        #print("Base class var : ", super().__init__(11))
        #print("Baase class var : ",Base.var)     ERROR
        print("Derived class var : ",self.var)
        

obj = Derived(10)
obj.display()
obj.useofsuper()

"""
parent init invoked
Derived init invoked
Base class var :  10
Derived class var :  10
Derived class var :  15
"""