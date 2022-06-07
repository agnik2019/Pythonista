def lengthOfLongestSubstring(s,k):
    """
    :type s: str
    :rtype: int
    """
    count = {}
    left,res, numDistict= 0,0,0
    for right in range(len(s)):
        if s[right]not in count:
            numDistict += 1
        count[s[right]] = count.get(s[right],0)+1
        
        while numDistict > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                numDistict -= 1
            left += 1
        res = max(res,right-left+1)
    return res

print(lengthOfLongestSubstring("araaci",2))
print(lengthOfLongestSubstring("araaci",1))
print(lengthOfLongestSubstring("cbbebi",3))