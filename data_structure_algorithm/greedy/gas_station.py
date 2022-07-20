from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start,summ,diff = 0,0,0
        for i in range(len(gas)):
            summ = summ+gas[i]-cost[i]
            if summ < 0:
                start = i+1
                diff +=summ
                summ = 0
        return start if summ+diff >= 0 else -1