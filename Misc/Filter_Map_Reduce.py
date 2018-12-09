#Filter
arr = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, arr))
# output: evens = [2,4,6]


#Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
# output: squared = [1,4,9,16,25]

#Reduce
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# output: product = 24
