import numpy as np

arr_3d = np.arange(125).reshape((5, 5, 5))


print("Array 3D:")
print(arr_3d)


print("Nilai pada index x=3, y=4, z=3:", arr_3d[3, 4, 3])


print("Nilai pada index x=2, y=0, z=1:", arr_3d[2, 0, 1])

print("Nilai pada index x=4, y=3, z=2:", arr_3d[4, 3, 2])
