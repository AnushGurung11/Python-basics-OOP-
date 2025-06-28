# Example of Inheritance 


class Animal: 
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        self.species = ""
    
    def Intro(self): 
        print(f"Hello, my name is {self.name} and I am {self.age} years old")
    
    def Speak(self): 
        print("Speaking")

class Human(Animal): 
    # Using super() method for calling the constructor from parent class 
    def __init__(self, name, age,race):
        super().__init__(name, age)
        self.race = race

    def Speak(self):
        print("I am talking")

class Dog(Animal): 
    def Speak(self):
        print("I am barking")
    
# Creating objects of each 
a1 = Animal("Animal",1)
a1.Intro()
a1.Speak()

h1 = Human("Anush",19,"Mongolian")
h1.Intro()
h1.Speak()
print(h1.race)

d1 = Dog("Numi",1)
d1.Intro()
d1.Speak()

     