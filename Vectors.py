import numpy as np

# # rank 1 array
# # (5,)
a = np.random.rand(5)

print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))

# # rank 2 array
# (5,1)
b = np.random.rand(5,1)

print(b)
print(b.shape)
print(b.T)
print(np.dot(b, b.T))

assert(b.shape == (5,1))

assert(a.shape == (5,1))
a = a.reshape((5,1))
assert(a.shape == (5,1))