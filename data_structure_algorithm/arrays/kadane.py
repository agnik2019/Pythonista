# largest continuos subarray sum

def subarraysum(arr):
    msf = 1e7
    meh = 0
    for i in range(len(arr)):
        meh = max(meh,arr[i]+meh)
        msf = max(msf,meh)
    return msf
