class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = {}
        def dfs(i,canBuy):
            if i >= len(prices):
                return 0
            if (i,canBuy) in dp:
                return dp[(i,canBuy)]
            if canBuy:
                idle = dfs(i+1,canBuy)
                buy = dfs(i+1, not canBuy)-prices[i]
                dp[(i,canBuy)] = max(idle,buy)
            else:
                idle = dfs(i+1,canBuy)
                sell = (prices[i] - fee) +dfs(i+1, not canBuy)
                dp[(i,canBuy)] = max(idle,sell)
            return dp[(i,canBuy)]
        return dfs(0,True)
        