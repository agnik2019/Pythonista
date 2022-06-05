class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        include = nums[0]
        exclude = 0
        for i in range(1,len(nums)):
            newinclude = exclude+nums[i]
            newexclude = max(include,exclude)
            include = newinclude
            exclude = newexclude
        return max(include,exclude)