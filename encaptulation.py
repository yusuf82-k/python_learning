class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property
  def display_age(self):
      print(self.__age)

p1 = Person("Emil", 25)
print(p1.name)
#print(p1.__age) # This will cause an error

#we have to use a class method to get access to the private property
p1.display_age()