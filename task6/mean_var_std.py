import numpy

X,M = map(int, input().strip().split())
l = []

for i in range(X):
    a = list(map(int, input().strip().split()))
    l.append(a)

l = numpy.array(l)

numpy.set_printoptions(sign=' ')
print(numpy.mean(l, axis = 1))
print(numpy.var(l, axis = 0))
print(numpy.std(l))
