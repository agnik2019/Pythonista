class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palidrome(s):
            return s== s[::-1]

        l,r = 0,len(s)-1
        while l<r:
            if s[l] != s[r]:
                delete_l = s[l+1:r+1]
                delete_r = s[l:r]
                return is_palidrome(delete_l) or is_palidrome(delete_r)
            l = l+1
            r = r-1
        return True


s = "abca"
