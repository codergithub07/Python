import numpy as np


# Defining array 1
a = np.array([[1, 2],
              [3, 4]])

# Defining array 2
b = np.array([[4, 3],
              [2, 1]])



# Adding 1 to each element of a
print("Array 'a' after adding 1 to each element: ", a + 1)


# Performing unary operation to add all elements of the array
print("Sum of all elements of the array: ", a.sum())


# Performing binary operation to add arrays 'a' & 'b'
print("Array 'a' + Array 'b': ", a + b)


c = np.array([1, 2])


print(c.dtype)