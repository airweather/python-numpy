import math
import numpy as np
import matplotlib.pyplot as plt

def linear_function(x):
    a = 0.5
    b = 2

    return a * x + b

# print(linear_function(5))

x = np.arange(-10, 10, 0.1)
y = linear_function(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Linear Function')
# plt.show()

def quadratic_function(x):
    a = 1
    b = -1
    c = -2

    return a * x ** 2 + b * x + c

# print(quadratic_function(2))

# x = np.arange(-10, 10, 0.1)
# y = quadratic_function(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Quadratic Function')
# plt.show()

def cubic_function(x):
    a = 4
    b = 0
    c = -1
    d = -8

    return a * x ** 3 + b * x ** 2 + c * x + d

x = np.arange(-10, 10, 0.1)
y = cubic_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Function')
plt.show()