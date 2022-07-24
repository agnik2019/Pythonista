def maximalSquare(matrix):
    row,col = len(matrix),len(matrix[0])
    dp = [[0]*(col+1) for _ in range(row+1)]
    ans = 0
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == "1":
                dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1])+1
                ans = max(ans, dp[r+1][c+1])
    return ans ** 2




matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))