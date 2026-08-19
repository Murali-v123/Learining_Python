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