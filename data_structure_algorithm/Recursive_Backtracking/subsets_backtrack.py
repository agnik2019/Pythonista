def subset(nums):
    res = []
    def backtrack(index,path):        
        res.append(path.copy())
        for i in range(index,len(nums)):
            path.append(nums[i])
            backtrack(i+1,path)
            path.remove(nums[i])
            
    backtrack(0,[])
    return res

nums = [1,2,3]
print(subset(nums))