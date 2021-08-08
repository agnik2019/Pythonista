from typing import NamedTuple


class Iter:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current


x = Iter(5)
itr = iter(x)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

