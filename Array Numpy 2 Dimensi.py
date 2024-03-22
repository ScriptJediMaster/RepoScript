import numpy as np


arr_2d = np.array([[1, 5, 4, 3, 2],
                    [2, 1, 5, 4, 3],
                    [3, 2, 1, 5, 4],
                    [4, 3, 2, 1, 5],
                    [5, 4, 3, 2, 1]])


print("Array 2D:")
print(arr_2d)


print("Block array yang diwarnai:")
print(arr_2d[0:5, 0:5])
