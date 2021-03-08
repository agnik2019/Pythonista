#itertools: product, permutation, combinations, groupby, and infinite iterators
from itertools import product
a = [1,2]
b= [3,4]
prod = product(a,b)
print(list(prod))