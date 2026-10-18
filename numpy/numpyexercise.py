import numpy as np

arr=np.array([1,2,3,4,5,6])
print(arr,type(arr))

# Creating an array of different data types 
arr1=np.array([1,2,3,4,5,6,"hello",False])
print(arr1,type(arr1),arr1.dtype)
arr.shape

# creating 2D matrix  matrix 
d=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(d)
d.shape
d.dtype

# A matrix that is full of zeros 
arr1=np.zeros((2,3),dtype=int)
print(arr1)

# Create a matrix that is full of ones. 
arr2=np.ones((2,3))
arr2

# Generates a matrix that is full of numbers, 100 
arr4=np.full((3,4),100)
arr4

# Creates an Identity matrix 
arr5=np.eye(3,dtype=int)
arr5

# generates an array from 0 to 10 with a gap of 2
arr6=np.arange(0,10,2)
arr6

# generating a 3 numberes arr here number 3 can be any number so that we can generate n numbers b/w the range we give
arr7=np.linspace(1,100,3)
arr7

# random numer generating 
# rng=np.random.default_rng()
# arr3 = rng.random((2,3))
arr3=np.random.random_integers(low=0,high=50,size=(2,3))
arr3=np.random.rand(2,3)
arr3

# Properties of a NumPy array 
arr.shape
arr.size
arr.dtype
# to know the dimensions
arr2.ndim

arr8=arr.astype(np.float64)
arr8
arr8.dtype

#array reshaping 
arr2d=np.array([[1,2,3],[4,5,6]])
arr2d
arr2d.shape
arr2d.reshape(3,2)
arr2d.flatten()

# 1d array inexing
arr = np.array([1,2,3,4,5])
print(arr[3])
print(arr[0])
print(arr[4])
idx=[1,0,4]
# fancy indexing
print(arr[idx])   
print(arr[arr%2!=0])
print(arr[arr%2==0])

# slicinng
print(arr[1:arr.size:2])



# 2d array indexing
arr2d=np.array([[1,2,3],[4,5,6]])
print(arr2d[1][2])
print(arr2d[0][1])

# list creates a copy and changes value in copy array
arr=[1,2,3,4,5]
sub=arr[1:3]
sub[0]=200
arr
sub

# numpy does not creates a copy and changes value in original array
arr=np.array([1,2,3,4,4,5])
sub=arr[1:3]
sub[0]=200
arr
sub

arr=np.array([1,3,5,2,8,6,"hello"])
print(arr.dtype)
carr = np.array([ 2 + 3j ])
carr1 = np.array([ 3 + 9j ])
print(carr+carr1,carr.dtype)

darr=np.array(["hello",{1,2,3,},5,6])
print(darr.dtype)

# agg fun
arr=np.array([1,2,3,4,5])
print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))

#power fun
print(np.sqrt(arr))
print(np.square(arr))
print(np.pow(arr,4))

# log fun

print(np.log(arr))
print(np.log10(arr))
print(np.log2(arr))
print(np.exp(arr))

print(np.round(3.14))
print(np.ceil(3.14))
print(np.floor(3.14))
print(np.unique(arr))
print(np.sort(arr))
print(np.abs(arr))