#without magic function __str__ ,printing an object shows its memory address
#adding __str__ shows what we want to show\
class Person:
    def __init__(self,first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def display(self):
        print(f"{self.first_name} {self.last_name} {self.age}")
    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.age}"
p1=Person("Harry" ,"Brook",34)
p1.display()
print(p1)