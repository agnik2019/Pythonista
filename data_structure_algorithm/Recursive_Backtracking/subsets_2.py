def subset(nums):
    res = []
    nums.sort()
    def backtrack(index,path):        
        res.append(path.copy())
        for i in range(index,len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1,path)
            path.remove(nums[i])
            
    backtrack(0,[])
    return res

nums = [1,2,2]
print(subset(nums))