#Asignment 15

#QUE 1

class Base:
    def __init__(self):
        print("parent init invoked")

class Derived(Base):
    def __init__(self):
        print("Derived init invoked")

obj = Derived()
"""
Derived init invoked
"""