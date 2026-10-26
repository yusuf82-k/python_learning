class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print(f"{self.brand},{self.model},{self.year}")
class Bus(Car):
    def __init__(self,brand,model,year):
        Car.__init__(self,brand,model,year)
    def display(self):
        Car.display(self)
bus1=Bus("savar","234",25)
bus1.display()