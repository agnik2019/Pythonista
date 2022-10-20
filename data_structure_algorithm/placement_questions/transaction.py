A = [1,-1,0,-105,1]
D = ["2020-12-31","2020-04-04","2020-04-04","2020-04-04","2020-07-12"]

def solve(A,D):
    # transaction number k  
    credit = [0]*13
    debit = [0]*13
    count = [0]*13

    for i,j in zip(A,D):
        yr,mn,day = j.split('-')
        mn = int(mn)
        count[mn]+= 1
        if i<0: credit[mn]+= i
        else: debit[mn] += i
    
    e = 0
    for i in range(1,13):
        if count[i]>=3 and credit[i]+debit[i]>=100:
            e += 1

    res = sum(credit)+sum(debit)-5*(12-e) 
    return res

print(solve(A,D))
        