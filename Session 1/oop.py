class Car:
    def __init__(self, brand,model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f'Brand = {self.brand} \nModel = {self.model} \nYear = {self.year}\n\n') 
        


cars = [
    Car('Toyota', 'Camry', '2020'),
    Car('Honda', 'Civic', '2019'),
    Car('BMW', 'Series 3', '2022')
]

for car in cars:
    car.display_info()