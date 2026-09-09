class InstanceTypes:
    collegeName="CEC " #Class variable is shared by all instances of the class
    def __init__(self,name):
        self.name=name
        self.course="Aiml"#instance variable 

    def show(self):
        print(f"hey Bhaii Tera Nam {self.name} aur tere course hai {self.course} aur tere collge ka naam hai {self.collegeName}")

a=InstanceTypes("Murali")
a.show()
InstanceTypes.collegeName="nit"#changes varible value for all instances of the class
print(a.collegeName)
a.course="cse"#only changes value for specific a only not for b
print(a.course)
print(a.name)
a.show()
b=InstanceTypes("Bro")
b.show()