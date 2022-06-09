class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        l, res = 0,0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            cost = (r-l+1) - max(freq.values())
            if cost <= k:
                res = max(res, r-l+1)
            else: 
                freq[s[l]] -= 1
                if freq[s[l]] == 0: del freq[s[l]]
                l += 1
        return res
            
        