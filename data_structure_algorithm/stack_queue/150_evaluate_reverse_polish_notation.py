from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token not in "+-/*":
                st.append(int(token))
                print(st)
            else:
                a = st.pop()            
                b = st.pop()
                if token == "+":
                    st.append(a+b)
                elif token == "-":
                    st.append(b-a)
                elif token == "*":
                    st.append(a*b)
                else:
                    st.append(int(float(b)/a))
                print(st)
        return st.pop()
tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))
