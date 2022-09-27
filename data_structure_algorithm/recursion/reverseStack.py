def reverse(st):
    if len(st)!=0:
        tmp = st.pop()
        reverse(st)
        insertAtBottom(st,tmp)

def insertAtBottom(st,item):
    if len(st)==0:
        st.append(item)
    else:
        tmp = st.pop()
        insertAtBottom(st,item)
        st.append(tmp)

st = [2,3,4,5,6]
reverse(st)
print(st)