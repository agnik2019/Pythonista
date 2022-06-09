def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)):
        nums[i] = -1 if nums[i] == 0 else 1
    # Now the problem reduces to longest subsarray having sum 0\
    #print(nums)
    mp,k = {},0
    sum, res = 0,0
    for i,num in enumerate(nums):
        sum += num
        if sum == k:
            res = i+1
        if sum-k in mp:
            res = max(res,i-mp[sum-k])
        if sum not in mp:
            mp[sum] = i
    return res

nums = [0,0,1,0,0,0,1,1]
print(findMaxLength(nums))