def gen(n):
    for i in range(n):
        yield i

x = gen(5)
print(next(x))
print(next(x))
print(next(x))



# generator use case
def csv_reader(filename):
    for row in open("filename","r"):
        yield row



# generator comprehension
x = (i for i in range(10))
print(x)
print(next(x))
print(next(x))
print(next(x))
