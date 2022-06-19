class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        i = 0
        while i<n:
            if nums[i] > 0: break
            l = i+1
            r = n-1
            while l<r:
                summ = nums[l]+nums[i]+nums[r]
                if summ == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l+1<n and nums[l+1] == nums[l]: l+=1
                    l += 1
                    r -= 1
                elif summ < 0:
                    l += 1
                else: r -= 1
            while i+1 <n and nums[i+1] == nums[i]: i+= 1
            i+= 1
        return res