# Time complexity -> O(n^2)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1e7] * len(nums)
        dp[0] = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]+j >= i:
                    dp[i] = min(dp[j]+1,dp[i])
        return dp[-1]
                
        