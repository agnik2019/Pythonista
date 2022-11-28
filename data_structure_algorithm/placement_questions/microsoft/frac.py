import math
x = [1,1,2,1,2]
y = [3,2,3,2,4]
# op-> 1
def solve(x,y):
    mp = {}
    count = 0
    for i in range(len(x)):
        g = math.gcd(int(x[i]),int(y[i]))
        x[i] //= g
        y[i] //= g

    for a,b in zip(x,y):
        key = str(a)+'/'+str(b)
        key2 = str(b-a)+'/'+str(b)
        if key2 in mp:
            count += mp[key2]
        mp[key] = mp.get(key,0)+1
    return count
    

print(solve(x,y))