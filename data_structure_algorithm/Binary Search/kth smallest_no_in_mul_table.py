class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def feasible(mid):
            count = 0
            for i in range(1,m+1):
                add = min(mid//i,n)
                count += add
            return count >= k
        left,right = 1,m*n
        while left < right:
            mid = left + (right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left
        