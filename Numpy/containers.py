xs = [3, 1, 2]
print xs, xs[2]
print xs[-1]
xs[2] = 'foo'
print xs
xs.append('bar')
print xs
x = xs.pop() # Remove and return the last element of the list
print x
print xs

nums = range(5)
print nums
print nums[2:4] # Get a slice from index 2 to 4 (exclusive)
print nums[2:]
print nums[:2]
print nums[:]
print nums[:-1]
nums[2:4] = [9, 8]
print nums

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print '%d: %s' % (idx+1, animal)

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares

squares = [x ** 2 for x in nums] # list comprehension
print squares

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares
odd_squares = [x ** 2 for x in nums if x % 2 != 0]
print odd_squares

d = {'cat': 'cute', 'dog': 'furry'}
print d['cat']
print 'cat' in d
d['fish'] = 'wet'
print d
print d.get('monkey', 'N/A')
print d.get('fish', 'N/A')
del d['fish']
print d.get('fish', 'N/A')

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)

for k, v in d.iteritems():
    print k, v

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x %2 == 0}
print even_num_to_square

animals = {'cat', 'dog'}
print 'cat' in animals
print 'fish' in animals
animals.add('fish')
print 'fish' in animals
animals.add('cat')
print len(animals)
animals.remove('cat')
print animals

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums

d = {(x, x+1) : x for x in range(10)}
t = (5, 6)
print d
print type(t)
print d[t]
print d[(7, 8)]