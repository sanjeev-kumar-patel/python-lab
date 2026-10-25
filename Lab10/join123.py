# Write a program to make 1D and 2D arrays using numpy and perform Array 
# Shape, Array Reshape, Array Iterating, Join, Split, Array filter.

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2)

print("\nShape of 1D Array:", arr1.shape)
print("Shape of 2D Array:", arr2.shape)

reshaped = arr1.reshape(5, 1)
print("\nReshaped Array:")
print(reshaped)

print("\nArray Iteration:")
for value in arr1:
    print(value, end=" ")

arr3 = np.array([60, 70, 80])
joined = np.concatenate((arr1, arr3))
print("\n\nJoined Array:")
print(joined)

split_arrays = np.array_split(joined, 3)
print("\nSplit Arrays:")
for part in split_arrays:
    print(part)

filtered = arr1[arr1 > 25]
print("\nFiltered Array:")
print(filtered)
