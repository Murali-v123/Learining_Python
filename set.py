import numpy as np

numbers=np.arange(1,11)
number1=np.arange(11,21,2)
num=set(numbers.tolist())
num1=set(number1.tolist())
num2={1,2,3}

# set opertions
print(num.union(num1))
print(num.difference(num1))
print(num.intersection(num1))
# prints numbers that are in either set but not both
print(num.symmetric_difference(num1))
# prints True if num is a subset of num1, False otherwise
print(num.issubset(num1))
print(num2.issubset(num))
# prints True if num is a superset of num2, False otherwise
print(num.issuperset(num2))

# adds all elements of num1 to num
num.update(num1)
print(num)

print(num.pop())

# prints True if num and num1 have no elements in common, False otherwise
print(num.isdisjoint(num1))