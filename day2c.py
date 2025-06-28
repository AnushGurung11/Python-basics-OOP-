# Example of class variable which is available for the class only 

class Student: 
    num=0
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

# Creating the object 
# class attribute can be accessed by using instance of the class and by the class name itself 
obj1 = Student("Anush",19)
print(Student.num)