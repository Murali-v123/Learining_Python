s="  HELLO world! "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace('H','x'))
print(s.count('L'))
print('ababababa'.count('a'))

#to count number of vowels in a string
s=input("enter input: ")
s2=s.lower()
a=s2.count('a')
i=s2.count('i')
o=s2.count('o')
e=s2.count('e')
u=s2.count('u')
print(f"Number of vowel:{a+e+i+o+u}")