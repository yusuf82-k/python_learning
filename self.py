class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        #accessing multiple attribute using self
        print(f"{self.brand},{self.model},{self.year}")
car=Car("BMW",22,2020)
car.display()