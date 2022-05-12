class Solution(object):
    def maxProfit(self, given_k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp = {}
        def dfs(i,canBuy,k,given_k):
            if i >= len(prices) or k >= given_k:
                return 0
            if (i,canBuy,k) in dp:
                return dp[(i,canBuy,k)]
            if canBuy:
                idle = dfs(i+1,canBuy,k,given_k)
                buy = dfs(i+1, not canBuy,k,given_k)-prices[i]
                dp[(i,canBuy,k)] = max(idle,buy)
            else:
                idle = dfs(i+1,canBuy,k,given_k)
                sell = prices[i]+dfs(i+1, not canBuy,k+1,given_k)
                dp[(i,canBuy,k)] = max(idle,sell)
            return dp[(i,canBuy,k)]
        return dfs(0,True,0,given_k)
        