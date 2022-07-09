class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        def feasible(distance):
            i,j,count = 0,0,0
            while i<n or j<n:
                while j<n and nums[j]-nums[i]<=distance:
                    j += 1
                count += (j-i-1)
                i += 1
            return count >= k
        left,right = 0,nums[-1]-nums[0]
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left