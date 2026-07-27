i=1
while(i<=10):
    print(f"the value is {i}")
    i+=1

i=0
while(i<=20):
    if(i%2!=0):
        print(f"The number is {i}")
    else:
        i+=1
        continue
    i+=1
# Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."

seats=8
while(seats>0):
    book=input("Do you want to book a seat? (yes/no): ")
    if(book.lower()=="yes"):
        print("Your ticket is booked")
        seats-=1
    elif(book.lower()=="no"):
        print("Thank you for visiting")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    seats-=1
if(seats):
    print("all seats are not boooked")
else:
    print("all seats are boooked")

time=10
while(time>0):
    print(f"the time is {time}")
    time-=1 
print("Happy new year")
