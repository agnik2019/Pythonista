def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)-1
    i = n
    while i and nums[i-1]>= nums[i]:
        i -= 1
    j = n
    while j>i and i and nums[i-1]>= nums[j]:
        j -= 1
    nums[i-1],nums[j] = nums[j],nums[i-1]
    j = n
    while i<j:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1

num = 123
arr = []
num = str(num)
for c in num:
    arr.append(int(c))
nextPermutation(arr)
print(arr)
str_c = ""
for c in arr:
    str_c += str(c)
print(int(str_c))

