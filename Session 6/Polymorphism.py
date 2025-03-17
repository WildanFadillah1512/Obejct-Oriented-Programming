class Vehicle:
    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Moves with four wheels"

class Bicycle(Vehicle):
    def move(self):
        return "Moves with two wheels"

class Boat(Vehicle):
    def move(self):
        return "Moves on water"

vehicles = [Car(), Bicycle(), Boat()]

for v in vehicles:
    print(v.move())

class UserAuthentication:
    def login(self):
        return "Login successful"

class EmailPasswordAuthentication(UserAuthentication):
    def login(self):
        return "Login successful with Email and Password"

class GoogleAuthentication(UserAuthentication):
    def login(self):
        return "Login successful with Google"

class FingerprintAuthentication(UserAuthentication):
    def login(self):
        return "Login successful with Fingerprint"

auth_methods = [EmailPasswordAuthentication(), GoogleAuthentication(), FingerprintAuthentication()]

for auth in auth_methods:
    print(auth.login())
