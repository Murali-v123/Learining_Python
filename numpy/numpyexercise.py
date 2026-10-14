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