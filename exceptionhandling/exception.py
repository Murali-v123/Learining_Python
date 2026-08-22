# # ynatx
# try:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code 

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


try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")


a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])  
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")


try:
    # Risky operation: dividing string by number
    res = "100" / 20 
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")


def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)