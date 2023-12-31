import math
import numpy as np
import matplotlib.pyplot as plt

def linear_function(x):
    a = 0.5
    b = 2

    return a * x + b

# print(linear_function(5))

# x = np.arange(-10, 10, 0.1)
# y = linear_function(x)

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

# x = np.arange(-10, 10, 0.1)
# y = cubic_function(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Quadratic Function')
# plt.show()

def my_func(x):
    a = 1
    b = -3
    c = 10

    return a * x ** 2 + b * x + c

# x = np.arange(-10, 10, 0.1)
# y = my_func(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.scatter(1.5, my_func(1.5))
# plt.text(1.5-1.5, my_func(1.5)+10, 'min value of f(x)\n({}, {})'.format(1.5, my_func(1.5)), fontsize=10)
# plt.title('my_func')
# plt.show()

# min_val = min(y)
# print(min_val)

def get_minimum(x1, x2, f):
    x = np.arange(x1, x2, 0.01)
    y = f(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('get_minimum')
    plt.show()

    return min(y)

# print(get_minimum(1, 4, my_func))

def exponential_function(x):
    a = 4
    return a ** x

# print(exponential_function(4))

# x = np.arange(-3, 2, 0.1)
# y = exponential_function(x)

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(-1, 15)
# plt.xlim(-4, 3)
# plt.title('exponential_function')
# plt.show()

def exponential_function(x):
    a = 4
    return math.pow(a, x)

# print(exponential_function(4))
# print(exponential_function(0))

# print(math.exp(4))
# print(np.exp(4))

# value, base
# print(math.log(2,3))

# 상용로그
# print(np.log2(4))

# base 가 e인 자연로그
# print(np.log(4))

# 역함수

# x = np.arange(-1, 5, 0.01)
# y1 = np.exp(x)

# x2 = np.arange(0.000001, 5, 0.01)
# y2 = np.log(x2)

# y3 = x

# plt.plot(x, y1, 'r-', x2, y2, 'b-', x, y3, 'k--')

# plt.ylim(-2, 6)
# plt.axvline(x=0, color='k')
# plt.axhline(y=0, color='k')

# plt.xlabel('x')
# plt.ylabel('y')

# plt.show()

# x = np.arange(-10, 10, 0.01)
# y1 = -np.log(x)
# y2 = -np.log(1-x)

# plt.axvline(x=0, color='k')
# plt.axhline(y=0, color='k')

# plt.grid()
# plt.plot(x, y1, 'b-', x, y2, 'r-')
# plt.text(0.9, 2.0, 'y1 = -ln(x)', fontsize=10)
# plt.text(0.1, 3, 'y1 = -ln(x)', fontsize=10)
# plt.xlim(-0.3, 1.4)
# plt.ylim(-0.5, 4)
# plt.scatter(0.5, -np.log(0.5))
# plt.show()




