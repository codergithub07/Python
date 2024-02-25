import numpy as np

arr = np.array([[[0, 1, 2, 3],
                 [10, 11, 12, 13]],
                 
                 [[100, 101, 102, 103],
                 [110, 111, 112, 113]],
                 
                 [[200, 201, 202, 203],
                  [210, 211, 212, 213]]])

# print(arr[1, 1, 1])   # Testing positin of an element


# Get no. of dimensions :-

    # print(np.ndim(arr))




# Getting total size of the array :-

    # print(np.size(arr))




# Getting shape of the array :-

print("The array having 3 sub lists, 2 sub lists in each list, 4 elements in each can be denoted as :\n", np.shape(arr))