for i in range(5):
    print(i);
    if(i==3):
        break
    # if we dont use break statement then the else block will also be executed after the for loop
else:
    print("Hello world")

for i in range(1,10):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        if(j==10):
            print("------------")
        
    if(i==6):
        break
else:
    print("The multiplication table has been printed upto 6")