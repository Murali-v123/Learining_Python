# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.
l=["bisi bele bath", "ragi mudde", "dosa", "idli", "vangi bath"]
upl=[x.upper() for x in l]
print(upl)
# Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

dict={
    "mobile":1500,
    "clothes":1000,
    "bike":10000,
    "car":1300,
    "house":1090,
}
sum=0
for val in dict.values():
    sum+=val
print(sum)

# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.

l=[1,2,3,4,5,6,7,8,9,10]
nl=[x**2 for x in l]
print(nl)

# Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

students = [
    {"name": "Aarav", "age": 15, "marks": 88},
    {"name": "Diya", "age": 16, "marks": 94},
    {"name": "Vivaan", "age": 15, "marks": 79}
]

for student in students:
    print(f"Name:{student['name']},Age:{student['age']},Marks:{student['marks']}")

# Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.
cities = {
    "Bengaluru": 12000000,
    "Mysuru": 920000,
    "Hubballi": 900000,
    "Mangaluru": 600000,
    "Belagavi": 800000
}
fdict={city:pop for city,pop in cities.items() if pop>700000}
print(fdict)

# In this example, the string is split only twice. The rest of the string remains as the final element.
sentence = "Python is fun to learn"
words = sentence.split(" ", 2)
print(words)


# Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matrix:
    print(i)

for i,row in enumerate(matrix):
    rsum=sum(row)
    print(f"Sum of row {i+1} is {rsum}")