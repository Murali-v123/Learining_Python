# a=int(input("Enter value A:"))
# b=int(input("Enter value B:"))

# try:
#     a/b
# except Exception as e:
#     print(e)
# else:
#     print("Executed sucessfully")
# finally:
#     print("The block which will print without any interaction of error")


# # Age Verifier:

# # Ask the user for their age.
# # If age is valid (number), show in how many years they will be 100 years old.
# # Handle invalid input gracefully.Age Verifier:

# # Ask the user for their age.
# # If age is valid (number), show in how many years they will be 100 years old.
# # Handle invalid input gracefully.
while(True):
    try:
        age=int(input("Enter your age: "))
        print(f"After {100-age} years your age will be 100")
    except ValueError:
        print("Enter a valid number")
    except Exception as e:
        print(e)
    else:
        print("You have entered only numbers")
        break
while(True):
    try:
        a=int(input("Enter value A:"))
        b=int(input("Enter value B:"))
        print(a/b)
    except ZeroDivisionError:
        print("Don't enter zero")
    else:
        print("Executed sucessfully")
        break
    finally:
        print("The block which will print without any interaction of error")

