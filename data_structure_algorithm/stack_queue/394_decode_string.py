class Solution:
    def decodeString(self, s: str) -> str:
        st, curstr, curdigit = [],"",0
        for c in s:
            if c == '[':
                st.append(curstr)
                st.append(curdigit)
                curstr = ""
                curdigit = 0
            elif c == ']':
                num = st.pop()
                prevstr = st.pop()
                curstr = prevstr+num*curstr
            elif c.isdigit():
                curdigit = curdigit*10+int(c)
            else:
                curstr += c
        return curstr
                
        