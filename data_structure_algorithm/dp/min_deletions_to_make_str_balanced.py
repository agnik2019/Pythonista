class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        b_count = 0
        for c in s:
            if c == 'b':
                dp.append(dp[-1])
                b_count += 1
            elif c == 'a':
                dp.append(min(dp[-1]+1,b_count))
        return dp[-1]
                
        