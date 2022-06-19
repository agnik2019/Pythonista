def removeKdigits( num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    st = []
    for n in num:
        while st and k and st[-1]>n:
            st.pop()
            k -= 1
        st.append(n)
    if k: st = st[0:-k]
    return ''.join(st).lstrip('0') or '0'

num = "10200"
k = 1
print(removeKdigits(num,k))