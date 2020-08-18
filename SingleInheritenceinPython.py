class Employee:

    noOfLeaves = 8

    def __init__(self,name,role,salary):
           self.name = name
           self.salary = salary
           self.role = role

    def printDetails(self):
        return f'Hey your name is {self.name} and your role  is {self.role} and your salary is {self.salary}'

    @classmethod
    def changeOfleaves(cls,newleaves):
           cls.noOfLeaves = newleaves 

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        #print(params)
        return cls(params[0],params[1],params[2])
    
    @staticmethod
    def printgood(string):
        print('This is good'+string)  
        return 'Hii' 


class Programmer(Employee):
    noOfHoliday = 32

    def __init__(self,name,role,salary,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

        
    def printprog(self):
        return f'The programmer name is {self.name} salary is {self.salary} and role is {self.role} and they know {self.languages}'
    

rohan = Employee('Roha',355,'Cordinator')
harry = Employee('Harry',255,'Instructor')
shubham = Programmer('Shubham',555,'Programmer',['Python','HTML',"CSS",'Java'])
karan = Programmer('Karan',777,'Programmer',['python','C++','C','Java'])
print(karan.printprog())
print(karan.noOfHoliday)
#print(karan.printDetails())

#print(karan.noOfLeaves)
#karan = Employee.from_str('Karan-355-Cordinator')
#print(karan.printgood('Harry'))
#print(karan.salary)
#print(karan.printDetl('Karan'))

#ravi = Employee('Ravi','CSE','Developer',50000)
#print(ravi.printDetl('Harry'))
#rohan = Employee('Rohan','Computer Science Engineering','Developer',50000)
#print(rohan.salary)
# print(rohan.noOfLeaves)
# rohan.changeOfleaves = 12
# print(rohan.changeOfleaves)
# print(rohan.noOfLeaves)
#print(rohan.printDetails())
# print(rohan.name)
# print(rohan.qalification)
# print(rohan.salary)
# rohan = Employee()
# rohan.name = 'Rohan'
# rohan.qalification = 'Computer Science Engineering'
# rohan.role = 'Developer'
# rohan.salary = 50000

# print(rohan.salary)
# print(rohan.noOfLeaves)
