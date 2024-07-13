#adding more functions in a class

#Creating a class
class Employees:
    
    def __init__(self, name, subname, birth_date):
        self.name = name
        self.subname = subname
        self.birth_date = birth_date
    
    def name_complete(self):
        return self.name + ' ' + self.subname

#Creating objects 
user1 = Employees('Helena', 'Barroca', '12/09/1940')
user2 = Employees('Marina', 'Barroca', '16/09/2004')
user3 = Employees('Fernando', 'Barroca', '10/09/1974')

#print 
#print(user1.name + ' ' + user1.subname)
print(user1.name_complete())
print(Employees.name_complete(user1))