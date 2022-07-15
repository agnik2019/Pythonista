# s = "aab"
# p = "c*a*b"
# return True if string s and pattern p matches else False
def regex_match(s,p):
    def dfs(i,j):
        if i>=len(s) and j>= len(p):
            return True
        if j >= len(p):
            return False
        match = i<len(s) and (s[i] == p[j] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == "*":
            return (dfs(i,j+2) or (match and dfs(i+1,j)))
        if match:
            return dfs(i+1, j+1)
        return False
    return dfs(0,0)

# Top Down memoization

def regex_match_dp(s,p):
    cache = {}
    def dfs(i,j):
        if (i,j) in cache:
            return cache[(i,j)]
        if i>=len(s) and j>= len(p):
            return True
        if j >= len(p):
            return False
        match = i<len(s) and (s[i] == p[j] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == "*":
            cache[(i,j)] = (dfs(i,j+2) or (match and dfs(i+1,j)))
            return cache[(i,j)]
        if match:
            cache[(i,j)] = dfs(i+1, j+1)
            return cache[(i,j)]
        cache[(i,j)] = False
        return False
    return dfs(0,0)

s = "aab"
p = "c*a*b"
print(regex_match_dp(s,p))