# TODO Creating a class called Vehicle and adding class methods 
# TODO create class attribute and methods 

class Vehicle:
    # Class Attribute 
    total_vehicle=0

    # Constructor for the class 
    def __init__(self,name,model):
        self.name = name 
        self.model = model 
        Vehicle.add_vehicle()


    @classmethod
    def add_vehicle(cls): 
        Vehicle.total_vehicle+= 1 

    @classmethod
    def show(cls): 
        return Vehicle.total_vehicle
    
# Creating an vehicle object and calling the class methods 
v1 = Vehicle("Tesla","X")
print(v1.name)
print(Vehicle.show())