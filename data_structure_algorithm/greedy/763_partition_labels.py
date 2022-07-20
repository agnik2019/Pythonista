from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        mp = {s[i]:i for i in range(L)}
        ans, i = [],0
        while i < L:
            j,end = i+1,mp[s[i]]
            while j < end:
                end = max(end,mp[s[j]])
                j += 1
            ans.append(end-i+1)
            i = end+1
        return ans