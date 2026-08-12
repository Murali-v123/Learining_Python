# Create a BankAccount class with private attributes for account_number and balance.
# Add methods to check balance, deposit, and withdraw funds.
# Try accessing the balance directly and observe the result.
class BankAccount:
    def __init__(self,holdername,acntnumber,balance):
        self.__balance=balance
        self.__acntnumber=acntnumber
        self.__holdername=holdername

    def check_balance(self):
        print(f"AccountHolder:{self.__holdername} has Rs$:{self.__balance}")

    def withdraw(self,amount):
        if(self.__balance<amount):
            print("Insufficient funds")
        else:
            self.__balance-=amount
            print(f"Amount withdraw Successful and balance left is {self.__balance}")

    def deposit(self,amount):
        self.__balance+=amount
        print(f"AccountNumber:{self.__acntnumber} has deposited {amount} suceesfully Balance:{self.__balance}")

    def display_details(self):
        print(f"AccountHolderName:{self.__holdername}")
        print(f"AccountNumber:{self.__acntnumber}")
        print(f"AccountBalance:{self.__balance}")

kb=BankAccount("Murali",1234565,500000)
kb.check_balance()
kb.display_details()
kb.withdraw(20000)
kb.deposit(100000)


class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self.__password

user = User("dev_karnataka", "pass1234")
print(user.get_username())  # Access allowed
print(user.check_password("wrong_pass"))  # Returns False
print(user.check_password("pass1234"))  # Returns True