class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_sum = [0]*n
        right_sum = [0]*n
        res = [0]*n
        left_sum[0] = height[0]
        right_sum[n-1] = height[n-1]
        for i in range(1,n):
            left_sum[i] = max(left_sum[i-1],height[i])
        for i in range(n-2,-1,-1):
            right_sum[i] = max(right_sum[i+1],height[i])
        summ = 0
        for i in range(1,n):
            res[i] = min(left_sum[i],right_sum[i])-height[i]
            summ += res[i]
        return summ 
            
        