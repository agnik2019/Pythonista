class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            summ = (summ + n) % k
            if summ in dic:
                if i - dic[summ] >= 2:
                    return True
            else:
                dic[summ] = i               
        return False