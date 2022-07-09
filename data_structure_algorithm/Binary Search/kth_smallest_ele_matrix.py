class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        def countLessOrEqual(x):
            cnt,c = 0,n-1
            for r in range(m):
                while c>=0 and matrix[r][c]>x:
                    c-= 1
                cnt += (c+1)
            return cnt >= k
        left,right = matrix[0][0],matrix[n-1][n-1]
        while left < right:
            mid = left+(right-left)//2
            if countLessOrEqual(mid):
                right = mid
            else:
                left = mid+1
        return left