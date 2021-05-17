import numpy
numpy.set_printoptions(sign=' ')

marray = numpy.array(input().split(),float)

print(numpy.floor(marray))
print(numpy.ceil(marray))
print(numpy.rint(marray))
