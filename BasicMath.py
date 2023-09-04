import math
import numpy as np
import matplotlib.pyplot as plt

def linear_function(x):
    a = 0.5
    b = 2

    return a * x + b

print(linear_function(5))

x = np.arange(-10, 10, 0.1)
y = linear_function(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function')
plt.show()