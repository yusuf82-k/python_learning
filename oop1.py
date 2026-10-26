class Person:

    def __init__(self,name,age):
        #we can set default values in the parameter
        #def __init__(self,name="YUSUF",age=22):
        #All the default parameter must be in the continuous sequences at
        #the end otherwise it will be syntax error
        #self must be the first parameter of all the methods inside the clas
        self.name =name
        self.age =age
    def greet(self):
        print("Hello my name is "+ self.name)

person1=Person("Yusuf",21)
person1.greet()
print(person1.age)
#The self parameter is a reference to the current instance of the class.

#It is used to access properties and methods that belong to the class.
