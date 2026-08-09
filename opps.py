class car:
    def __init__(self,carid,carname,carmodel,status="rented"):
        self.carid=carid
        self.carname=carname
        self.carmodel=carmodel
        self.status=status

    def display(self):
        print("Car ID:",self.carid)
        print("Car Name:",self.carname)
        print("Car Model:",self.carmodel)
        print("Car Status:",self.status)

    def updatecarstatus(self,status):
        self.status=status
        car.display(self)

# here we use self to refer to the current instance of the class. It allows us to access the attributes and methods of the class within its own methods. In this case, we use self to update the status of the car and then call the display method to show the updated information.
car1=car(101,"BMW","X5")
car1.display()
car1.updatecarstatus("Available")
car2=car(102,"Audi","A6")
car2.display()

# Create a Class:
# Write a class Mobile with attributes brand and price.
# Create two objects of the class and display their attributes using a method.

class Mobile:
    def __init__(self,brand,price=10000):
        # default parameter
        self.brand=brand
        self.price=price

    def display(self):
        print("Mobile Brand:",self.brand)
        print("Mobile Price:",self.price)

Samsung=Mobile("samsung",150000)
Samsung.display()

iphone=Mobile("Iphone")
iphone.display()

# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.

class Student:
    def __init__(self,name,marks=35):
        self.name=name
        self.marks=marks

    def display_info(self):
        print("Student Name: ",self.name)
        print("Student Mark: ",self.marks)

murali=Student("Murali",99)
murali.display_info()

gani=Student("Gani",90)
gani.display_info()

pradeep=Student("pradeep")
pradeep.display_info()

madhu=Student("Madhusudhan",100)
madhu.display_info()