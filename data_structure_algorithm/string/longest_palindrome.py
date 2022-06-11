def ispalindrome(s,i,j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def longestpalindrome_bf(s):
    if len(s) == 1:
        return s
    res = ""
    maxlen = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if ispalindrome(s,i,j):
                if maxlen < j-i+1:
                    maxlen = j-i+1
                    res = s[i:j+1]              
    return res


def longestPalindromedp(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    ans = s[i] # last char
    for start in range(n-1,-1,-1):
        for end in range(start+1,n):
            if s[start] == s[end]:
                if end-start ==1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    if len(ans) < end-start+1:
                        ans = s[start:end+1]
    return ans


s = "cbbd"
print(longestpalindrome_bf(s))