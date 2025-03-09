class Vehicle:
    def __init__(self, brand, model, rental_rate):
        self.brand = brand
        self.model = model
        self.rental_rate = rental_rate
    
    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def open_trunk(self):
        return "Trunk is open."

class Bike(Vehicle):
    def kickstart(self):
        return "Bike kickstarted."

class LuxuryFeatures:
    def enable_gps(self):
        return "GPS enabled."
    
    def enable_heated_seats(self):
        return "Heated seats enabled."

class LuxuryCar(Car, LuxuryFeatures):
    def __init__(self, brand, model, rental_rate, luxury_charge):
        super().__init__(brand, model, rental_rate)
        self.luxury_charge = luxury_charge
    
    def calculate_rental(self, days):
        return super().calculate_rental(days) + (self.luxury_charge * days)

def main():
    while True:
        print("\nVehicle Rental System")
        print("1. Rent a Car")
        print("2. Rent a Bike")
        print("3. Rent a Luxury Car")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            brand = input("Enter vehicle brand: ")
            model = input("Enter vehicle model: ")
            rental_rate = float(input("Enter rental rate per day: "))
            days = int(input("Enter number of rental days: "))
            vehicle = Car(brand, model, rental_rate)
        
        elif choice == "2":
            brand = input("Enter vehicle brand: ")
            model = input("Enter vehicle model: ")
            rental_rate = float(input("Enter rental rate per day: "))
            days = int(input("Enter number of rental days: "))
            vehicle = Bike(brand, model, rental_rate)
        
        elif choice == "3":
            brand = input("Enter vehicle brand: ")
            model = input("Enter vehicle model: ")
            rental_rate = float(input("Enter rental rate per day: "))
            luxury_charge = float(input("Enter luxury charge per day: "))
            days = int(input("Enter number of rental days: "))
            vehicle = LuxuryCar(brand, model, rental_rate, luxury_charge)
        
        elif choice == "4":
            print("Exiting system...")
            break
        
        else:
            print("Invalid choice! Please try again.")
            continue
        
        print(f"Total rental cost: {vehicle.calculate_rental(days)}")
        
        if isinstance(vehicle, Car):
            print(vehicle.open_trunk())
        if isinstance(vehicle, Bike):
            print(vehicle.kickstart())
        if isinstance(vehicle, LuxuryCar):
            print(vehicle.enable_gps())
            print(vehicle.enable_heated_seats())

if __name__ == "__main__":
    main()
