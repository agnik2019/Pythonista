def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    mp = {}
    sum, count = 0,0
    for num in nums:
        sum += num
        if sum == k:
            count += 1
        if sum-k in mp:
            count += mp[sum-k]
        mp[sum] = mp.get(sum,0)+1
    return count