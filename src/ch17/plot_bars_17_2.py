from matplotlib import pyplot as plt
import numpy as np

# With lists
centers = [1, 2, 3, 4, 5]
tops = [2, 4, 6, 8, 10]

plt.bar(centers, tops)
plt.show()

# With NumPt arrays
centers = np.arange(1, 6)
tops = np.arange(2, 12, 2)

plt.bar(centers, tops)
plt.show()

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4,
}

plt.bar(fruits.keys(), fruits.values())
plt.show()
