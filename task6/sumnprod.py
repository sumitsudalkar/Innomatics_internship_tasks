import numpy
X, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(X)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))
