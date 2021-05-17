import numpy
X = int(input())
A = numpy.array([input().split() for _ in range(X)], float)
print(round(numpy.linalg.det(A),2))
