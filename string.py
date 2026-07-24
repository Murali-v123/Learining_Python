#string slicing
'''s = "python"
print(s[::3])
print(s[::-1])
print(s[0])
print(s[1:-1])
print(s[2::3])
print(s[1])
print(s[-1])
print(s[1:3])
print(s[:3])
print(s[:-1])
print(s[2:])'''

'''s="  HELLO world! "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace('H','x'))
print(s.count('L'))
print('ababababa'.count('a'))'''

'''
s=input("enter input: ")
s2=s.lower()
a=s2.count('a')
i=s2.count('i')
o=s2.count('o')
e=s2.count('e')
u=s2.count('u')
print(f"Number of vowel:{a+e+i+o+u}")
'''
#a=input("enter the input:")
#print("a" in a)
'''
a=int(input("enter the number 1:"))
b=int(input("enter the number 2:"))
#print( a>10 and b>10)
#print( a<5 or b<5)
#print(not (a>b))
print(a&b)
print(a|b)
print(a^b)
print(a>>1)
print(a<<1)'''

#list homework
'''
li=["apple","banana","cat","dog","elephant"]
li.append("fish")
li.insert(-1,"goat")
print(li)
li.remove(li[2])
print(li)'''
'''
l=[1,2,5,6,7,3,4,9,11,3]
l.sort()
l.reverse()
print(l)'''

#tuple hw
'''
t=("apple","banana","cat","dog","elephant")
#slicing
print(t[1:3])

#set hw
s={"apple","banana","cat","dog","elephant"}
s1={"pple","anana","at","og","elephant"}
s2=s1|s
s3=s & s1
s4=s-s1
s.add("fish")
print(s2)
print(s3)
print(s4)
print(s)
s.remove("apple")
print(s)
s.discard("og")
print(s)
s.pop()
print(s)
s.clear()
print(s)
print(type(s))
'''
#converting from list to tuple and set
'''
g=[1,2,"hello"]
s=set(g)
t=tuple(g)
print(f"set is {s}")
print(f"tuple is {t}")
s.add(5)
print(s)'''

#dictionary
'''
kar = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "kolar":"mulagal dosa",
    "bangarpet":"chats"
}
print(kar)
#to add
kar["kgf"]="kushka"
kar["bangarpet"]="onion"
#to update
kar["Bengaluru"]="bisi"
kar.update(kar)
print(kar)
#to delete an value
del kar["kolar"]
kar.pop("bangarpet")
print(kar)
#print(kar.keys())
#print(kar.values())
#print(kar.items())'''
