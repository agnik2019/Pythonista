class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recur(idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            for i in range(idx,len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i]
                recur(idx+1)
                nums[i],nums[idx] = nums[idx],nums[i]
        recur(0)
        return res
