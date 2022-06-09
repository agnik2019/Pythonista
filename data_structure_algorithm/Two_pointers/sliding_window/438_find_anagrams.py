from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        mp = Counter(p)
        left, matched = 0,0
        res = []
        for right in range(len(s)):
            if s[right] in mp:
                mp[s[right]] -= 1
                if mp[s[right]] == 0:
                    matched += 1
            
            if matched == len(mp):
                res.append(left)
            if right >= len(p)-1:
                if s[left] in mp:
                    if mp[s[left]] == 0:
                        matched -= 1
                    mp[s[left]] += 1
                left += 1
        return res
        