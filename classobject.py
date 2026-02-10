#Class is a blueprint of an object.
#Object is an instance of a class-It follows the class

class Student:
    #Attributes
    name= "Joy"
    age= 23
    gender= "Female"
    course= "MIT"

    #Behaviour/Functions
    def study(self):
        print("Student is studying")
        

student1= Student() #This is how to create an object
student1.study()
print(student1.name)

student2= Student()
student2.study()
