class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        freq = {}
        l,res = 0,0
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r],0)+1
            while len(freq)>2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1
            res = max(res, r-l+1)
        return res