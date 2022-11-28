class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for p in path.split('/'):
            if p == "" or p== ".":
                continue
            elif p == '..':
                if st: st.pop()
                else: continue
            else:
                st.append(p)
        return "/"+"/".join(st)
                
        