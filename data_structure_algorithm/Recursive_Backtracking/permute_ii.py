def permute2(nums):
    res = []
    def backtrack(nums,path):
        if not nums:
            res.append(path.copy())
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
    backtrack(nums,[])
    return res

nums= [1,2,3]
print(permute2(nums))