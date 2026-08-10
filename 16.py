# Create a Class with a Constructor:

# Write a class Movie with attributes title and rating using the __init__() constructor.
# Define a method to display the movie’s title and rating.
# Add Default Parameters:

class Movie:
    def __init__(self, title, rating=7):
        self.title = title
        self.rating = rating

    def display_info(self):
        print(f"The movie name is {self.title} and has the rating of {self.rating}")

pushpa=Movie("Pushpa",9.8)

july=Movie('July',8.9)
mirchi=Movie("Mirchi")
mirchi.display_info()
july.display_info()

pushpa.display_info()

# Create a class Employee with attributes name, designation, and salary (default value of salary is 30,000).
# Write a method that displays the details of each employee.
# Create multiple Employee objects with different values for name and designation, and test the default salary behavior.

class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def info_display(self):
        print(f"The Name of th employee is {self.name} and with his designation {self.designation} and has a salary of {self.salary}")

e1=Employee("pradeep","debugger")
e2=Employee("rohith","tester",50000)
e3=Employee("murali","sde",90000)

e1.info_display()
e2.info_display()
e3.info_display()
        