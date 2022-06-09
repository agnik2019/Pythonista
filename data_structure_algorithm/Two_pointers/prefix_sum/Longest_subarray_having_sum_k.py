# Longest subarray having sum k
def LongestsubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    mp = {}
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

arr = [10, 5, 2, 7, 1, 9]
k = 15
print("Length =", LongestsubarraySum(arr, k))