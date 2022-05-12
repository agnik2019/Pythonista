class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = {}
        def dfs(i,canBuy,k):
            if i >= len(prices) or k >= 2:
                return 0
            if (i,canBuy,k) in dp:
                return dp[(i,canBuy,k)]
            if canBuy:
                idle = dfs(i+1,canBuy,k)
                buy = dfs(i+1, not canBuy,k)-prices[i]
                dp[(i,canBuy,k)] = max(idle,buy)
            else:
                idle = dfs(i+1,canBuy,k)
                sell = prices[i]+dfs(i+1, not canBuy,k+1)
                dp[(i,canBuy,k)] = max(idle,sell)
            return dp[(i,canBuy,k)]
        return dfs(0,True,0)