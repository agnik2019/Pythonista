import sys
x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i:i**2, x)

# print(y)
# print(list(y))

# print(sys.getsizeof(y))
# print(sys.getsizeof(list(y)))

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(y.__next__())  #dunder method

print('for loop starts...')

# for elem in y:
#     print(elem)


# identical for loop
while True:
    try:
        print(next(y))
    except StopIteration:
        print('done')
        break

