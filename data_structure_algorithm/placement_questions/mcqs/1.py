def f(n):
    if n<= 1:
        print(n)
    else:
        f(n/2)
        print(n%2)

print(f(173))