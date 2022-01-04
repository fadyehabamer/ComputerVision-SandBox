import numpy as np

# 2d-array
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# random arr
arr = np.arange(12).reshape(3, 4)
print(arr)
print(arr.size)   # total items
print(arr.shape)  # row*col
print(arr.ndim)   # how many dimensions
print(arr.dtype)  # type of data in array
print(arr.itemsize) # number of items in each col
