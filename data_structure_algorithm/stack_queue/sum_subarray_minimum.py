def sumSubarrayMins(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    summ = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])
            mn = min(arr[i:j+1])
            summ+= mn
    return summ


arr = [3,1,2,4]
print(sumSubarrayMins(arr))