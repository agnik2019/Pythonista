class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums)-k
        def quick_select(l,r):
            pivot,p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p],nums[i] = nums[i],nums[p]
                    p += 1
            nums[p],nums[r] = nums[r],nums[p]
            if k>p: return quick_select(p+1,r)
            elif k<p: return quick_select(l,p-1)
            else: return nums[p]
        return quick_select(0,len(nums)-1)