#tuples
t=("apple","banana","cat","dog","elephant")
#tuple slicing
print(t[1:3])

# #set hw
s={"apple","banana","cat","dog","elephant"}
s1={"jug","zeebra","cat","orange","elephant"}
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
print(s.discard("og"))
# print(s)
s.pop()
print(s)
s.clear()
print(s)
print(type(s))

# #converting from list to tuple and set

g=[1,2,"hello"]
s=set(g)
t=tuple(g)
print(type(g))
print(f"set is {s}")
print(f"tuple is {t}")
s.add(5)
print(s)
