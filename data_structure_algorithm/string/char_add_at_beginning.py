'''
Minimum Characters required to make a String Palindromic
'''



class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        def computeLPS(s):
            lps = [0]*len(s)
            i,j = 1,0
            while i<len(s):
                if s[i] == s[j]:
                    lps[i] = j+1
                    i += 1
                    j += 1
                elif j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1] 
            return lps
        tempstr = A+'#'+A[::-1]
        lps = computeLPS(tempstr)
        #print(lps)
        return len(A)-lps[-1]
