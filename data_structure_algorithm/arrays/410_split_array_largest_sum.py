class Solution(object):
    def valid(self, nums, maxsum, m):
        cnt = 1
        subarraysum = 0
        for num in nums:
            subarraysum += num
            if subarraysum > maxsum:
                cnt += 1
                subarraysum = num
                if cnt > m:
                    return False
        return True
                
            
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if m == 0:
            return sum(nums)
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            if self.valid(nums,mid,m):
                high = mid-1
            else:
                low = mid + 1
        return low 
        

'''
Similar questions:  
1011. Capacity To Ship Packages Within D Days


'''