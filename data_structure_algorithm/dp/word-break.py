class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        worddic = set(wordDict)
        dp = [False]* (len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in worddic:
                    dp[i] = True
                    break
        return dp[-1]
        