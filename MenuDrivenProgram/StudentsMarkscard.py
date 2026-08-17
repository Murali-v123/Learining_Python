class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.__marks = {}


    def get_Marks(self):
        return self.__marks

    def addmarks(self, subject, marks):
        self.__marks[subject] = marks

    def calculateAvg(self):
        total = 0
        for mark in self.__marks.values():
            total += mark
        avg=total / len(self.__marks)
        return avg

    def is_passed(self):
        has_passed = all(mark >= 35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calculate_Grade(self):
        print("Grade",end="")
        percentage=self.calculateAvg()
        if percentage>=90:
            print("A")
        elif percentage>=80 and percentage<90:
            print(" B")

class Report_Card:
    @staticmethod
    def generate(student:Student):
        stud_mark=student.get_Marks()
        print(student.name)
        print("Marks")
        for sub,mar in stud_mark.items():
            print(f"{sub}:{mar}")
        print("------------------")
        print(f"Average:{student.calculateAvg():.2f}")
        student.is_passed()
        student.calculate_Grade()

a=Student("kl",2)
a.addmarks("MAths",90)
a.addmarks("English",80)


Report_Card.generate(a)
