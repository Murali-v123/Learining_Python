#  1. Single Responsibility Principle (SRP)
# SRP Practice: Create a Book class that only stores details. Create another class that prints book details.

class Book:
    def __init__(self,bookname,author):
        self.bookname=bookname
        self.author=author

class bookdetails(Book):
    def get_details(self):
        print(f"Book Name:{self.bookname} and it's author name is:{self.author}")

B=bookdetails("Python","chd")

B.get_details()

# 2. Open/Closed Principle (OCP)
#  Build a billing system that calculates tax based on ProductType. Add Food, Electronics, etc., using subclasses.

class Tax:
    def tax(self):
        pass

class Food(Tax):
    def tax(self):
           print("you have ordered Food and has a tax of 5%")

class Electronics(Tax):
     def tax(self):
            print("The ProductType is Electronic and has a tax of 15%")


f=Food()
f.tax()

e=Electronics()
e.tax()

# 3. Liskov Substitution Principle (LSP)
#LSP Practice: Write a class Vehicle and subclasses like Bike, Boat. Avoid breaking behavior.

class Vehicle:
     def Break(self):
        pass

class Bike(Vehicle):
     def Break(self):
          print("Bike has been applied the break")

class Boat(Vehicle):
     def Break(self):
          print("Sorry Boat has been no breaks")

b=Bike()
b.Break()

c=Boat()
c.Break()


#  4. Interface Segregation Principle (ISP)
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")

h=Human()
h.work()
h.eat()

r=Robot()
r.work()

# 5. Dependency Inversion Principle (DIP)
class InputDevice:
    def input(self):
        pass

class Keyboard(InputDevice):
    def input(self):
        return "User typing..."

class Mouse(InputDevice):
    def input(self):
        return "Mouse clicked"

class Computer:
    def __init__(self, device: InputDevice):
        self.device = device

    def get_input(self):
        return self.device.input()

c=Computer(Mouse())
c.get_input()

c=Computer(Keyboard())
c.get_input()