# input -> arr
import math
def warlane(arr, roadlen):
    max_diff = float("-inf")
    arr.sort()
    for i in range(len(arr)-1):
        max_diff = max(max_diff,arr[i+1]-arr[i])
    max_diff = math.ceil(max_diff/2)
    return max(arr[0]-1,max_diff,roadlen-arr[-1])


print(warlane([1,4,4,6],6))