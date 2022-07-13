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
        nums.sort(reverse = True)
        
        #sorting the array in descending order
        #so if first value is greater than target, it will not be included in any subset
        #so we cant partition the entire array into k equal sum subsets
        if nums[0] > target:
            return False
        
        dp = {}
        def backtrack(i,k,rem):
            #since subproblem depends on used indices of array
            #if same subproblem occurs again just return dp value
            if tuple(used) in dp:
                return dp[tuple(used)]
            if k == 0:
                return True
            if rem == 0:
                partition = backtrack(0,k-1,target)
                dp[(tuple(used),rem)] = partition
                print(dp)
                return partition
            for j in range(i,len(nums)):
                if not used[j] and rem-nums[j] >= 0:
                    used[j] = True
                    if backtrack(j+1,k,rem-nums[j]):
                        return True
                    used[j] = False
            dp[tuple(used)] = False
            return False
        
        return backtrack(0,k,target)
nums = [4,3,2,3,5,2,1] 
k = 4
print(Solution().canPartitionKSubsets(nums,k))

        