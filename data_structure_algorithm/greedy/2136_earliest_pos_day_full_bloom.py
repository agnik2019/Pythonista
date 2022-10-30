# 2136. Earliest Possible Day of Full Bloom
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        mx,time = 0,0
        for g,p in sorted(zip(growTime,plantTime),reverse=True):
            time += p
            mx = max(mx,time+g)
        return mx