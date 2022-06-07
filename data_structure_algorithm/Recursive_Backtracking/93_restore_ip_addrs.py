def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    if len(s) > 12:
        return res
    def backtrack(i,dots, curIp):
        if i == len(s) and dots == 4:
            res.append(curIp[:-1])
        if dots>4:
            return
        for j in range(i,min(i+3,len(s))):
            if int(s[i:j+1])<256 and (i == j or s[i] !='0'):
                backtrack(j+1,dots+1,curIp+s[i:j+1]+'.')
    backtrack(0,0,"")
    return res