class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target >= nums[low] and nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if target > nums[mid] and  target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
        