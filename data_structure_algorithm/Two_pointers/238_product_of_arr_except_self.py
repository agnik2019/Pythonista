def productExceptSelf( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # construct prefix product
    pre = [1] * (len(nums)+1)
    for i,num in enumerate(nums):
        pre[i+1] = num*pre[i]
    # construct suffix product
    suf = [1]*(len(nums)+1)
    for i in range(len(nums)-1,-1,-1):
        suf[i] = suf[i+1]*nums[i]
    print(pre)
    print(suf)
    res = []
    for i in range(len(pre)-1):
        res.append( pre[i]*suf[i+1])
    return res

nums = [1,2,3,4]
print(productExceptSelf( nums))