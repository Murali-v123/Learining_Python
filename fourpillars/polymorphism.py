# Polymorphism:
# Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area. Each class should calculate area differently based on its shape.
# Create a loop to calculate areas for both Circle and Rectangle objects.

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def calculate_area(self):
        print("Calculating area of Circle")

class Rectangle(Shape):
    def calculate_area(self):
        print("Calculating area of Rectangle")


shape=[Circle(),Rectangle()]
for c in shape:
    c.calculate_area()


class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()