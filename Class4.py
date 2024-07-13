#Creating constructors

#Creating a class
class Employees:
   def __init__(self, name, subname, birth_date):
      self.name = name
      self.subname = subname
      self.birth_date = birth_date


#Creating objects 
user1 = Employees('Helena', 'Barroca', '12/09/1940')
user2 = Employees('Marina', 'Barroca', '16/09/2004')
user3 = Employees('Fernando', 'Barroca', '10/09/1974')

#print 
print(user1.name)
print(user2.name)
print(user3.subname)