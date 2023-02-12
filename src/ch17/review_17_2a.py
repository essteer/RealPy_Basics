from matplotlib import pyplot as plt
import numpy as np

# 1 - page 500
xs = np.arange(1, 6)
plt.plot(xs)
# plt.show()

# 2 - page 501
xs = np.arange(1, 6)
ys = np.arange(2, 11, 2)
plt.plot(xs, ys)
# plt.show()

# 3 - page 502
xs = np.arange(1, 6)
ys = [3, -1, 4, 0, 6]
plt.plot(xs, ys)
# plt.show()

# 4 - page 503
xs = np.arange(0, 5)
ys = np.arange(2, 11, 2)
plt.plot(xs, ys, "g-o")
# plt.show()

# 5 - page 504 and 505
first = np.arange(1, 6)
second = [1, 2, 4, 8, 16]
plt.plot(first, "g-o")
plt.plot(second, "b-^")
# plt.show()

# 6 - page 507
array = np.arange(1, 21).reshape(5, 4)
plt.plot(array)
# plt.show()

# 7 - page 508
array = np.arange(1, 21).reshape(5, 4)
plt.plot(array.transpose())
# plt.show()

# 8 - page 509 to 513
other_site = np.arange(0, 21)
real_python = other_site ** 2
plt.plot(other_site)
plt.plot(real_python)
plt.xticks([0, 5, 10, 15, 20])
plt.xlabel("Days of Reading")
plt.ylabel("Amount of Python Learned")
plt.title("Python Learned Reading Real Python vs. Other Site")
plt.legend(["Other Site", "Real Python"])
# plt.show()

# 9 - page 515
xs = np.arange(1, 6)
ys = np.arange(2, 11, 2)
plt.bar(xs, ys)
# plt.show()

# 10 - page 517
fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4
}
plt.bar(fruits.keys(), fruits.values())
# plt.show()

# 11 - page 518
plt.hist(np.random.randn(10000), 20)
# plt.show()
