import numpy
X, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(X)])
B = numpy.array([list(map(int, input().split())) for n in range(X)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
