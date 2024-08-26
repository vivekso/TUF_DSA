import selectionSort
import random as rnd

l = rnd.sample(range(1,2**10), 10**3)
n = rnd.sample(range(1,2**10), 10**3)

print('descending',selectionSort.descending(l))
print('ascending',selectionSort.ascending(n))