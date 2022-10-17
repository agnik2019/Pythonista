def fact(n):     
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def ncr(n,r):
    return fact(n)/(fact(r)*fact(n-r-1))

def query(k,l,n):
    summ = 0
    for i in range(k,n+1):
        a = ncr(i-1,k-1)
        b = ncr(n-i,l-k)
        summ += i*a*b
    return summ


print(query(2,2,3))