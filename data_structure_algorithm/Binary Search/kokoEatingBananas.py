import math
from typing import List
def minEatingSpeed(piles : List[int], h:int) -> int:
        l,r = 1,max(piles)
        while l < r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                r = mid
            else:
                l = mid+1
        return r


piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))