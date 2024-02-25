from operator import index
import numpy as np


arr = np.array([[0, 1, 2, 3],
               [10, 11, 12, 13],
               [20, 21, 22, 23],
               [30, 31, 32, 33]])

print("Initial array is: \n", arr)


print("array with first 2 rows & alternate columns is : \n ", arr[:2, ::2])


index_array = arr[[1, 2, 0, 3],
                  [2, 1, 3, 0]]

print("Elements with indices (1, 2), (2, 1), (0, 3), (3, 0) : \n", index_array)