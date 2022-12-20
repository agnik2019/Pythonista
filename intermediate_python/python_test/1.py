nums = [1,2,1,3]
from collections import Counter
mp = Counter(nums)
print(mp)
res = []
for k,v in mp.items():
    if v == 1:
        res.append(k)
print(res)
