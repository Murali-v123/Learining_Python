class Employee:
    company="Apple"
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"Hey Bhaii Tera Nam {self.name} aur tere company ka naam hai {self.company}")

    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany

c1=Employee("Murali")
c1.show()
Employee.changeCompany("FAANG")
c1.show()
c2=Employee("Rohith")
c2.show()