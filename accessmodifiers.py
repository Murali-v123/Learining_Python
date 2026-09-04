# public,private and protected access modifiers
class A:
    def __init__(self):
        self.name="murali" #public variable
        self._age=20 #protected variable
        self.__bank_balance=150000 #private variable


    # can only be accessed within the class
    def show1(self):
        print(f"Balance:{self.__bank_balance}")

class B(A):
    def show(self):
        super()
        print("Name:",self.name) #accessing public variable
        print("Age:",self._age) #accessing protected variable
        # print("Bank Balance:",self.__bank_balance) #cannot access private variable

ab=B()
ab.show()
ab.show1()