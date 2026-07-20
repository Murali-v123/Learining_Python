#list ,tuple & dict
#list mutable
list1 = [1,2,8,9,3,10,5]
print("List:", list1)

#list methods
list1.append(6)
print("List after append:", list1)
list1.remove(3)
print("List after remove:", list1)
list1.insert(2, 10)
print("List after insert:", list1)
list1.pop()
print("List after pop:", list1)
list1.sort()
print("List after sort:", list1)
list1.sort(reverse=True)
print("List after sort in reverse:", list1)
list1.reverse()
print("List after reverse:", list1)
list1.clear()
print("List after clear:", list1)

# #tuple immutable
# tuple1 = (1,2,3,4,5)
# print("Tuple:", tuple1)

# #dictionary mutable
# dict1 = {"name":"John", "age":30, "city":"New York"}
# print("Dictionary:", dict1)