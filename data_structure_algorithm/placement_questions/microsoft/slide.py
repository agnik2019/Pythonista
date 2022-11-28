def solution(A):
    # write your code in Python 3.8.10
    s = set()
    n = len(A)
    for i in A:
        s.add(i)

    l = len(s)

    i = 0
    j = 0
    sol = float("inf")
    mp = {}
    tmp = 0

    while j<n:
        if A[j] in mp and mp[A[j]]:
            mp[A[j]]+=1
        else:
            mp[A[j]] = 1
            tmp += 1
        
        while tmp == l and i<n:
            sol = min(sol,j-i+1)
            mp[A[i]]-=1
            if not mp[A[i]] :
                tmp-=1
            i+=1
            
        j+=1

    return sol

print(solution([2,1,6,4,1,7,2,1,1,4,3,4,1]))