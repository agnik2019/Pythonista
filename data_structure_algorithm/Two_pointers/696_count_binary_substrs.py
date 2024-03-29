class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                groups.append(1)
            else:
                groups[-1] += 1
        res = 0
        for i in range(1,len(groups)):
            res += min( groups[i],groups[i-1])
        return res