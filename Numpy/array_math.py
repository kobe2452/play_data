import numpy as np

x = np.array([ [1,2], [3,4] ], dtype=np.float64)
y = np.array([ [5,6], [7,8] ], dtype=np.float64)

print x + y
print np.add(x, y)

print x - y
print np.subtract(x, y)

print x * y
print np.multiply(x, y)

print x / y
print np.divide(x, y)

print np.sqrt(x)

v = np.array([9, 10])
w = np.array([11, 12])

print v.dot(w)
print np.dot(v, w)

print x.dot(v)
print np.dot(x, v)

print x.dot(y)
print np.dot(x, y)

print x
print np.sum(x)
print np.sum(x, axis=0) # Compute sum of each column
print np.sum(x, axis=1) # Compute sum of each row

print x
print x.T

z = np.array([1, 2, 3])
print z
print z.T