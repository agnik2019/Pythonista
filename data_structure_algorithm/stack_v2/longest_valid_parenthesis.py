class Solution:
    def longestValidParentheses(self, s: str) -> int:
        is_ok = [0]*len(s)
        st = []
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            elif c==')':
                if st:
                    is_ok[st.pop()] = 1
                    is_ok[i] = 1
        maxi,summ = 0,0
        for i in range(len(is_ok)):
            if is_ok[i]== 1:
                summ += is_ok[i]
            else: 
                summ = 0
            maxi = max(summ,maxi)
        return maxi