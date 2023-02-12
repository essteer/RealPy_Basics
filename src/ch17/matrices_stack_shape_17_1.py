import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

np.vstack([a, b])
np.hstack([a, b])
a.reshape(6, 1)

nums = np.arange(1, 10)
matrix = nums.reshape(3, 3)

np.arange(1, 17).reshape(4, 4)
np.arange(1, 13).reshape(3, 2, 2)

arr = np.array([x for x in range(1, 24, 2)])
arr.reshape(3, 2, 2)

arr2 = np.arange(1, 24, 2).reshape(3, 2, 2)
