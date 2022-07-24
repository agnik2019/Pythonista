from typing import List
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mp,count = {},0
        for n1 in nums1:
            for n2 in nums2:
                mp[n1+n2] = mp.get(n1+n2,0)+1
        for n3 in nums3:
            for n4 in nums4:
                if -(n3+n4) in mp:
                    count += mp[-(n3+n4)]
        return count
        