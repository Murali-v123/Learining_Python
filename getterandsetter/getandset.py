# Getters and Setters:
# Create a class BankAccount with a private attribute balance.
# Write a getter method to retrieve the balance and a setter method to update it, ensuring the balance never goes below zero.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        print(f"Balance is {self.__balance}")

    def set_balance(self, amount):
        self.__balance += amount
        print(f"the balnce is {self.__balance}")


b = BankAccount(2000)
b.get_balance()
b.set_balance(25000)


# Write a class Calculator with a method multiply(). Allow it to take either two or three arguments to multiply two or three numbers.
class Calculator:
    def multiply(self, i, j, k=1):
        return i * j * k


mul = Calculator()
mul.multiply(3, 4, 5)
mul.multiply(9, 8)


# Create a parent class Shape with a method draw() that prints "Drawing shape".
# Create a child class Circle that overrides draw() to print "Drawing circle".


class Shape:
    def draw(self):
        print("Drawing shape")


class Circle(Shape):
    def draw(self):
        print("Drawing circle")


s = Shape()
s.draw()
c = Circle()
c.draw()

# Define an abstract class Employee with an abstract method calculate_salary().
# Create a subclass Manager that implements calculate_salary() based on working hours and rate per hour.
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self, hr: float, hrr: float):
        print(f"{hr * hrr:.2f}")


e = Manager()
e.calculate_salary(5, 50.5)


