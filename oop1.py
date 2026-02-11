class employee:
    #Attributes
    def  __init__(self,fullname,position,status,age):
        self.fullname= fullname
        self.position= position
        self.status= status
        self.age= age

    def work(self):
        print(self.fullname,"is working")
        

employee1 = employee("Mr.Ken Mwenda","MD","Married",45)
print(employee1.fullname,employee1.position,employee1.status,employee1.age,employee1.work())
employee2 = employee("Jean Kamau","Program Manager","Single",29)
print(employee2.fullname,employee2.position,employee2.status,employee2.age)
employee3 = employee("Mark Joe","Lecturer","Single",31) 
print(employee3.fullname,employee3.position,employee3.status,employee3.age)