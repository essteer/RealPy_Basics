from matplotlib import pyplot as plt
import numpy as np

# array = np.arange(1, 6)
# plt.plot(array)
# plt.show()

# data = np.arange(1, 21).reshape(5, 4)
# data now contains the following array:
# array([[ 1, 2, 3, 4],
# [ 5, 6, 7, 8],
# [ 9, 10, 11, 12],
# [13, 14, 15, 16],
# [17, 18, 19, 20]])
# plt.plot(data)
# plt.show()

data = np.arange(1, 21).reshape(5, 4)
plt.plot(data.transpose())
plt.show()
