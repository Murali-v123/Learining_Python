# # Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() method.
# Demonstrate how the Bike can use both start and ride.
class Vehicle:
    def start(self):
        print("Vehicle is beeing started")

class Bike(Vehicle):
    def __init__(self,name):
        self.name=name
    def ride(self):
        # super().start() calling parent class method using super keyword
        print("The bike is ready to ride")

b=Bike("pulsar")
b.start()
b.ride()

class Family:
    def __init__(self, surname):
        self.surname = surname

class Child(Family):
    def __init__(self, surname, name):
        super().__init__(surname)
        self.name = name

child = Child("Gowda", "Ajay")
print(f"{child.name} {child.surname}")

