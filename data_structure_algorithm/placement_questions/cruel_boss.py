def combo(n):
    dp = [-1]*(n+1)
    if n <3:
        return 1
    elif n == 3: return 2
    else:
        dp[0],dp[1],dp[2],dp[3] = 1,1,1,2
        for i in range(4,n+1):
            dp[i] = dp[i-1]+dp[i-3]
        return dp[n]


print(combo(2))
print(combo(4))
print(combo(6))