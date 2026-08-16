class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts={}

    def Create_Account(self,id,Holder_Name,Acctype):
        if(Acctype=="SavingsAccount"):
            new_account=SavingsAccount(id,Holder_Name)
        elif(Acctype=="CurrentAccount"):
             new_account=CurrentAccount(id,Holder_Name)
        self.__accounts[id]=new_account
        print(f"{Acctype} Created Sucessfully")
        return new_account

    def get_account(self,id):
        if id not in self.__accounts:
            print("Account Not Found")
        else:
            Account=self.__accounts[id]
            print(f"ID:{Account._id}\tName:{Account._Holder_Name}")

class Account:
    def __init__(self,id,Holder_Name):
        self._id=id
        self._Holder_Name=Holder_Name
        self._balance=0

    def Check_Balance(self):
        print(f"Balance is:{self._balance}")

    def Deposit(self,amount):
        self._balance+=amount
        print(f"Deposit successful Updated Balance is:{self._balance}")

    def Withdraw(self,amount):
            if self._balance>amount:
                self._balance-=amount
                print(f"WithDraw successful and Balnce is:{self._balance}")
            else:
                print("Funds are not enough,Sorry")

class SavingsAccount(Account):
    def Interst_Caluculator(self):
        interestrate=0.4
        interest=self._balance*interestrate
        print(f"Your interest rate is:{interestrate} ,and interest:{interest}")

class CurrentAccount(Account):
    def Withdraw(self,amount):
        Over_Draft=1000
        if Over_Draft+self._balance > amount:
            self._balance-=amount
            print(f"WithDraw successful and Updated Balance is:{self._balance}")
        else:
            print("Funds are not enough,Sorry")

kbl=Bank("Karanataka bank","bpet")

s1=kbl.Create_Account(1,"murali","SavingsAccount")
s2=kbl.Create_Account("2","gani","CurrentAccount")

s1.Deposit(10000)
s2.Deposit(1000)

s1.Withdraw(100)
s2.Withdraw(1020)

s1.Interst_Caluculator()

kbl.get_account(1)
kbl.get_account("2")