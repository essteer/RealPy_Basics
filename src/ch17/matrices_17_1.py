import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 3d array
matrix = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(2 * a)

b = np.array([[5, 4, 3], [7, 6, 5], [9, 8, 7]])
c = b - a
print(c)

d = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(d * d)
print(d @ d)

print(d.shape)
print(a.diagnoal())
print(b.flatten())
print(c.transpose())
print(a.min())
print(b.max())
print(c.mean())
print(d.sum())

