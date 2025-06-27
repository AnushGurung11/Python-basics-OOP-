# For the basics of OOP in Python 

# Creating a class named dog 

class Dog: 

    # This is considered as the constructor 
    def __init__(self):
        pass

    # Here self represents that this methods is only for the instance of the object
    def bark(self): 
        print("Bark")

# Creating an instance of class Dog 

d = Dog()
d.bark()