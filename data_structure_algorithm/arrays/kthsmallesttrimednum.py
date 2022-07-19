from typing import List
def smallestTrimmedNumbers(nums: List[str], queries: List[List[int]]) -> List[int]:
    def trimDigit(num,n):
        trimmed = num[-n:]
        return trimmed
    res = []
    for query in queries:
        k,trim = query[0],query[1]
        temp = [int(trimDigit(num,trim)) for num in nums]
        kthsmall = sorted(range(len(temp)), key = lambda sub: temp[sub])[k-1]
        res.append(kthsmall)
    return res

nums = ["24","37","96","04"]
queries = [[2,1],[2,2]]
print(smallestTrimmedNumbers(nums,queries))