class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res,ans = 0,s[n-1]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and ((j-i+1) < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if len(ans) < j-i+1:
                        ans = s[i:j+1]
        return ans