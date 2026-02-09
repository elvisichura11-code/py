#Functions/Methods- A block of code that is used to perform a 
#task.

#Standard library functions
y = max(45, 78, 89,76,99,54,87,89,344,98,34)
print("The maximum value is",y)

x= min(45, 78, 89,76,99,54,87,89,344,98,34)
print("The minimum number is", x)


#User-Defined Functions
def name():
    
    print("Elvis")
name() #calling a function by its name



def summation():
    print(10+20)

summation()


#parameters/variables
def dog(name,breed,age):
   
    print(name,breed,age,"yrs")

#Arguements- Values passed when calling the function
dog("Bob","German Shepherd",4) 
dog("Mary","Chihuahua",2)    
dog("Pinero","Siberian Husky",5)

print()


#Display the data of five employees
#full name,position,gender,age

def details(Fullname, position, gender,age):
    print("Fullname:",Fullname)
    print("position:",position)
    print("gender:",gender)
    print("age:",age)

details("Ruben Ismail","Secretary","Male",34)
print()
details("Joy Wanjau","Accountant","Female",27)
print()
details("Mohammed Salisu","Manager","Male",44)
print()
details("Karen Mukoba","C.E.O","Female",56)
print()
details("Stephen Karanja","Technician","Male",28)