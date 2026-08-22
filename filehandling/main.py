with open("myfile.txt","r") as file:
    f=file.read()
print(f)

with open("myfile.txt","a") as file:
    file.write("Hello, Python!\n")
    file.write("File handling \nis easy with Python.")
print("File written successfully")

# Checking File Properties
f = open("myfile.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)

try:
    file = open("geek.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()

# Create a File and Write
# Ask user for 3 friend names.
# Write them into friends.txt, one per line.

with open("friends.txt",'w') as file:
    for i in range(3):
        friend=input("Enter your friend name:")
        file.write(f"{friend}\n")
print("Sucessfully added your frnds list")

# Ask for student name and marks.
# Append the info to marks.txt in this format: Ravi - 85
with open("friends.txt",'a') as file:
    for i in range(3):
        friend=input("Enter your name:")
        marks=input("Enter your marks:")
        file.write(f"{friend} - {marks}\n")