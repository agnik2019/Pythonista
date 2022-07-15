from typing import List
# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         target = sum(nums)/k
#         used = [False]*len(nums)
#         def backtrack(i,k,subsetSum):
#             if k==0:
#                 return True
#             if subsetSum == target:
#                 return backtrack(0,k-1,0)
#             for j in range(i,len(nums)):
#                 if used[j] or subsetSum+nums[j]> target:
#                     continue
#                 used[j] = True
#                 if backtrack(j+1,k,subsetSum+nums[j]):
#                     return True
#                 used[j] = False
#             return False
#         return backtrack(0,k,0)



class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        used = [False]*len(nums)
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k

        dp = {}
        def backtrack(i,k,subsetsum):
            #since subproblem depends on used indices of array
            #if same subproblem occurs again just return dp value
            if tuple(used) in dp:
                return dp[tuple(used)]
            if k == 0:
                return True
            if subsetsum == target:
                partition = backtrack(0,k-1,0)
                dp[tuple(used)] = partition
                return partition
            for j in range(i,len(nums)):
                if not used[j] and subsetsum+nums[j] < target:
                    used[j] = True
                    if backtrack(j+1,k,subsetsum+nums[j]):
                        return True
                    used[j] = False
            dp[tuple(used)] = False
            return False
        
        return backtrack(0,k,0)
nums = [4,3,2,3,5,2,1] 
k = 4
print(Solution().canPartitionKSubsets(nums,k))

        