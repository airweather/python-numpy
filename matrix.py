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

# 삼각행렬
print(np.tri(3))

# 초기화 x
# 초기화가 없어서 배열 생성비용이 저렴하고 빠름
# 초기화되지 않아서 기존 메모리에 존재하는 값이 들어감
print(np.empty(10))

# like
print(np.zeros_like(a1))
print(np.ones_like(a2))
print(np.full_like(a3, 10))

# arange() : 정수 범위로 배열 생성
print(np.arange(0, 30, 2))

# linspace() : 범위 내에서 균등 간격의 배열 생성
# 0부터 1까지의 수를 5개로 나눠서
print(np.linspace(0, 1, 5))

# logspce() : 범위 내에서 균등간격으로 로그 스케일로 배열 생성
print(np.logspace(0.1, 1, 20))

# 실수값으로 랜덤 행렬 생선
print(np.random.random((3, 3)))

# 실수값으로 랜덤 행렬 생선
print(np.random.randint(0, 10, (3, 3)))

# 정규분포
print(np.random.normal(0, 1, (3, 3)))

# 균등분포
print(np.random.rand(3, 3))

# 표준 정규 분포
print(np.random.randn(3, 3))