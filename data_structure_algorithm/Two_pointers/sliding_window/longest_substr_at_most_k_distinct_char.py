def lengthOfLongestSubstring(s,k):
    """
    :type s: str
    :rtype: int
    """
    count = {}
    left,res= 0,0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1      
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        res = max(res,right-left+1)
    return res

print(lengthOfLongestSubstring("araaci",2))  # 4
print(lengthOfLongestSubstring("araaci",1))  # 2
print(lengthOfLongestSubstring("cbbebi",3))  # 5