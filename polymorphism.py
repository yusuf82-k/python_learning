class Dog:
    def speak(self):
        print("bark")
class cat:
    def speak(self):
        print("meow")
class tiger:
    def speak (self):
        print("roar")
doggy=Dog()
pussy_cat=cat()
prada=tiger()
for x in (doggy,pussy_cat,prada):
    x.speak()
#polymorphism