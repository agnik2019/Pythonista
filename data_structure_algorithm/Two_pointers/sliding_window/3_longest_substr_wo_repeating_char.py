def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    count = {}
    left,res= 0,0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        
        while count[s[right]] > 1:
            count[s[left]] = count.get(s[left],0) - 1
            left += 1
        res = max(res,right-left+1)
    return res