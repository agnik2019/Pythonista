from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        dict_t = Counter(t)
        remaining = len(dict_t)
        l, r = 0, 0
        ans = float("inf"), None, None

        for r in range(len(s)):
            dict_t[s[r]] -= 1
            if dict_t[s[r]]== 0:
                remaining -= 1

            while remaining == 0:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                dict_t[s[l]] += 1
                if s[l] in dict_t and  dict_t[s[l]] > 0:
                    remaining += 1
                l += 1    
  
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
