def subarraysDivByK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    freq = [0]*k
    freq[0] = 1
    sum,count = 0,0
    for num in nums:
        sum += num
        rem = sum % k
        if rem <0: rem += k
        count += freq[rem]
        freq[rem] += 1
    return count