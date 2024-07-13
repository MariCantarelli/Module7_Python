from datetime import datetime
#Calculating the age of an employee

#Creating a class
class Employees:
    
    def __init__(self, name, subname, birth_year):
        self.name = name
        self.subname = subname
        self.birth_year = birth_year
    
    def name_complete(self):
        return self.name + ' ' + self.subname

    def age_employees(self):
        year = datetime.now().year
        self.birth_year = int(year - self.birth_year)
        return self.birth_year

#Creating objects 
user1 = Employees('Helena', 'Barroca', '12/09/1940')
user2 = Employees('Marina', 'Barroca', '16/09/2004')
user3 = Employees('Fernando', 'Barroca', '10/09/1974')

#print 
print(Employees.age_employees(user1))
print(Employees.age_employees(user2))
print(Employees.age_employees(user3))