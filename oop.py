# For the basics of OOP in Python 

# Creating a class named dog 

class Dog: 

    # This is considered as the constructor 
    def __init__(self,name):
        """"Here the name is the paramenter which is to be passed during the creation of object of dog"""
        self.name = name 
        
    # creating getter functions 
    def get_name(self): 
        return self.name
    
    # creating setter function 
    def set_name(self, name): 
        self.name = name 
        
    

    # Here self represents that this methods is only for the instance of the object
    def bark(self): 
        print("Bark")

# Creating an instance of class Dog 

d = Dog("Numi")
print(d.get_name())
d.set_name("luci")
print(d.get_name())