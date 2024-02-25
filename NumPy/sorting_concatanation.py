import numpy as np

a = np.array([2, 4, 3, 1, 5])
b = np.array([7, 6, 8, 9, 10])

print(np.sort(a))

print(np.concatenate((np.sort(a), np.sort(b))))