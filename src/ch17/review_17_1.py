import numpy as np

# 1
A = np.arange(3, 12).reshape(3, 3)

# 2
print(A.min())
print(A.max())
print(A.mean())

# 3
B = A ** 2

# 4
C = np.vstack([A, B])

# 5 - calculate the matrix product of C by A
C @ A

# 6
C = C.reshape(3, 3, 2)
