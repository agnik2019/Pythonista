class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        mp = {}
        for k in nums3:
            for l in nums4:
                mp[k+l] = mp.get(k+l,0)+1
        count = 0
        for i in nums1:
            for j in nums2:
                if -(i+j) in mp:
                    count += mp[-(i+j)]
        return count