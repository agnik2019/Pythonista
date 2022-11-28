class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        is_ok =[0]*len(s)
        ans = ""
        for i,c in enumerate(s):
            if c == '(':
                st.append(i)
            elif c==')':
                if st:
                    is_ok[st.pop()] = 1
                    is_ok[i] = 1
            
        # we get our is_ok array
        # which signifies valid parenthesis
        for i,c in enumerate(s):
            if c in "()":
                if is_ok[i]:
                    ans += c
            else:
                ans += c
        return ans
        