import sys

x = [1,2,3,4,5,6,7,8,9,10]

print(sys.getsizeof(x))
print(sys.getsizeof(range(1,11)))

for element in x:
    print(element)

for i in range(1,11):
    print(i)