class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j == len(p): 
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == '?'):
                cache[(i,j)] =  dfs(i + 1, j + 1)
                return cache[(i,j)]
            if p[j] == '*':
                cache[(i,j)] =  dfs(i, j + 1) or i < len(s) and dfs(i + 1, j) 
                return cache[(i,j)]
            cache[(i,j)] = False
            return False

        return dfs(0, 0)