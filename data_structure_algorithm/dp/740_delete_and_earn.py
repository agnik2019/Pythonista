class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = max(nums)+1
        arr = [0]*N
        for num in nums:
            arr[num] += 1
        inc = 0
        exc = 0
        for i in range(0,N):
            newexc = max(inc,exc)
            newinc = exc + arr[i]*i
            inc = newinc
            exc = newexc
        return max(inc,exc)
