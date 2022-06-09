def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # longest subarray with at most k
    freq = {}
    l, res = 0,0
    for r in range(len(nums)):
        freq[nums[r]] = freq.get(nums[r],0)+1
        while 0 in freq and freq[0] > k and l <= r:
            freq[nums[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))
    