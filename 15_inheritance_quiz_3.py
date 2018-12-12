#Asignment 15

#QUE 3

class Base:
    def __init__(self, v):
        self.basevar = v
        print("parent init invoked")

class Derived(Base):
    def __init__(self,v):
        #super().__init__(v)
        self.dervar = v
        print("Derived init invoked")
    def display(self):
        #print("Base class var :",self.basevar)
        print("Derived class var :",self.dervar)
        

obj = Derived(10)
obj.display()

"""
File ".\15_inheritance_quiz_3.py", line 20, in <module>
    obj.display()
  File ".\15_inheritance_quiz_3.py", line 15, in display
    print("Base class var :",self.basevar)
AttributeError: 'Derived' object has no attribute 'basevar'
"""

"""
Derived init invoked
Derived class var : 10
"""