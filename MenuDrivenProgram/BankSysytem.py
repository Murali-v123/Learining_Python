balance=0
while(True):
    print("1.Create Account")
    print("2.Add Balance")
    print("3.Check Balance")
    print("4.WithDraw")
    print("5.Deposit")
    print("6.Exit")

    choice=int(input("Enter Your Choice:"))

    if(choice==1):
        print("Account Created Successfully") 

    elif(choice==2):
       amount=int(input("Enter Amount to Add:"))
       balance+=amount
       print(f"Amount added sucessfully and the balance is {balance}")
    elif(choice==3):
        print("Your Balance is:",balance)
    elif(choice==4):
        amount=int(input("Enter Amount to withDraw:"))
        while(amount>balance):
            print("Insufficient Balance")
            amount=int(input("Enter Amount to withDraw:"))
        balance-=amount
        print(f"Amount Withdrawn Successfully and the balance is {balance}")
    elif(choice==5):
        amount=int(input("Enter Amount to deposit:"))
        balance+=amount
    elif(choice==6):
        print("Thank You for Using Our Service")
        break
    else:
        print("Invalid Choice Try Again")
        