class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def display(self):
        print(self.fname,self.lname,self.age,end=" ")

class student(Person):
    def __init__(self,fname,lname,age,graduation_year):
        Person.__init__(self,fname,lname,age)
        self.graduation_year=graduation_year
    def display(self):
        Person.display(self)
        print(f"{self.graduation_year}")

    def grade(self):
        print(4.00)
student1=student("Yusuf","Hasan","22",2028)
student1.display()
student1.grade()