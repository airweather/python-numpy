import numpy as np

# 1차원
a1 = np.array([1, 2, 3, 4, 5])

print(a1)
# type은 ndarray
print(type(a1))
# (5개, 차원)
print(a1.shape)
# index로 접근 가능
print(a1[0], a1[1], a1[3])
a1[1] = 6
print(a1)

a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a2)
print(a2.shape)
print(a2[0, 2], a2[1][2])

a3 = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
])
print(a3)
print(a3.shape)

print(np.zeros(10))
print(np.ones(10))

print(np.ones((3,3)))

print(np.full((3, 3), 1.23))

# identity matrix
print(np.eye(4))

