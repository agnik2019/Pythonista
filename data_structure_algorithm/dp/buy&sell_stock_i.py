class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = {}
        k = 1
        def dfs(i,canBuy,k):
            if i >= len(prices) or k <=0:
                return 0
            if (i,canBuy) in dp:
                return dp[(i,canBuy)]
            if canBuy:
                idle = dfs(i+1,canBuy,k)
                buy = dfs(i+1, not canBuy,k)-prices[i]
                dp[(i,canBuy)] = max(idle,buy)
            else:
                idle = dfs(i+1,canBuy,k)
                sell = prices[i]+dfs(i+1, not canBuy,k-1)
                dp[(i,canBuy)] = max(idle,sell)
            return dp[(i,canBuy)]
        return dfs(0,True,k)