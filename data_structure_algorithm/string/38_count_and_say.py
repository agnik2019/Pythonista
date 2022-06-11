
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    res = "1"
    for _ in range(2,n+1):
        prev = res
        res = ""
        j = 0
        while j < len(prev):
            cur = prev[j]
            cnt = 1
            j += 1
            while j<len(prev) and cur == prev[j]:
                cnt += 1
                j += 1
            res += str(cnt)+str(cur)
    return res


for i in range(6):
    print(countAndSay(i))
