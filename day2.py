 
class Student: 
    
    # This is the constructor for the class Student  
    def __init__(self,name,age,grade):

        # Instance variables 
        self.name = name
        self.age = age
        self.grade = grade 
    
    # Creating getter and setter methods 
    def get_name(self):
        return self.name
    
    def get_age(self): 
        return self.age
    
    def get_grade(self): 
        return self.grade 
    
    def set_name(self, name): 
        self.name = name

    def set_age(self,age): 
        self.age = age

    def set_grade(self,grade): 
        self.grade = grade

# Creating a new class for course 
class Course:

    # Creating a Constructor for the class  
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        
        self.students = []

    # Creating a methods for storing the students in list 

    def add_students(self, student): 

        # Adding condition 
        if len(self.students) < self.max_students: 
            self.students.append(student)
            return True 
        return False 
    
    # Creating a methods for calcualting the avg of all the students grade 
    def avg_grade(self): 
   
        avg = 0

        for student in self.students: 
            avg += student.get_grade()
        
        return avg/len(self.students)
        
    
# Now creating student objects and adding them to the students list 
s1 = Student("Anush",19,100)
s2 = Student("Bibek",20,78)

c1 = Course("CHASA",40)

# Adding students 
c1.add_students(s1)
c1.add_students(s2)

print(c1.avg_grade())


    