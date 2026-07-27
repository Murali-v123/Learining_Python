
age=int(input("Enter your age: "))
gender=input("Enter your gender: ")

if(age<5):
    print("no need of buspass you can travel for free:😉")
elif(age>=60):
    print("Congratulations you get a senior citizen discount")
elif(gender=="female"):
    print("Your ticket is free")
else:
    print("You have to pay the full price")

time=(input("Enter the time in 24-hour format (0-23): "))
if(time=="8am"):
    print("its time for Breakfast")
elif(time=="1pm"):
    print("its time for lunch")
elif(time=="8pm"):
    print("its time for dinner")
else:
    print("Its not time for meal")


age=int(input("Enter Your Age: "))
if(age<=18):
    print("You get A student membership pass")
elif(age>=60):
    print("You get a senior citizen membership")
else:
    print("You get a regular membership")