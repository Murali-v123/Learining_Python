# Write a for loop that prints all multiples of 3 between 1 and 30.
for i in range(1,31):
    if(i%3==0):
        print(i)

# Sum of First 10 Numbers
sum=0
for i in range(1,11):
    sum+=i
    print(sum)

# Print Your Name Letter by Letter:
name="murali"
for i in name:
    print(name[i])

text=input("Enter the continuios string: ")
v="aeiouAEIOU"
count=0
for i in text:
    if i in v:
        count+=1
print(f"the vowels in the string is {count}")

