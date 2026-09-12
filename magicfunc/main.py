from magicfunctions import Employee

# using __str__functions
e=Employee("Murali",12)
print(e)

# using __len__ function
print(len("murali"))

print(str(e))
print(repr(e))

# 1. Define the updated class FIRST
#  e = Employee("Murali", 12)

# print(e)              # Uses __str__  -> Murali-12
# print(len(e))         # Uses __len__  -> 6 (Fixed to test your object, not the string!)
# print(repr(e))        # Uses __repr__ -> Employee('Murali', 12)

# emp_list = [e]
# print(emp_list)       # Uses __repr__ inside lists -> [Employee('Murali', 12)]
