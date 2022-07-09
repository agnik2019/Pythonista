class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def feasible(threshold):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total>threshold:
                    total = num
                    count += 1
                    if count>m:
                        return False
            return True
        left,right = max(nums),sum(nums)
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left
        
        