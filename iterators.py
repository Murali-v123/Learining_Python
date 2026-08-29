# nums=[1,2,3,4,5]

# for num in nums:
#     print(num)

class countdown:
    def __init__(self,count):
        self.count=count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<0:
            raise StopIteration
        num=self.count
        self.count-=1
        return num

movies=["pushpa","salaar","aarya","raaka"]
cnt=countdown(len(movies)-1)

for num in cnt:
    print(movies[num])

class Even:
    def __init__(self,count):
        self.count=count

    def __iter__(self):
        return self

    def __next__(self):
        while self.count>0:
            num=self.count
            self.count-=1
            if num%2==0:
                return num
        raise StopIteration

evn=Even(20)
for i in evn:
    print(i)

# Simple Generator Function

# Write a generator function countdown(n) that yields numbers from n to 0.
# Test it using a for loop.

def Simple_Generator(n):
    for i in range(n):
        yield i

for i in Simple_Generator(5):
    print(i)

# Create a generator expression to produce the squares of numbers from 1 to 10.
# Print the first 5 values using next()
ge=(x**2 for x in range(1,11))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(list(ge))

import sys
ge=(x**2 for x in range(1,100000))
ge1=[x**2 for x in range(1,100000)]
print(sys.getsizeof(ge))
print(sys.getsizeof(ge1))
