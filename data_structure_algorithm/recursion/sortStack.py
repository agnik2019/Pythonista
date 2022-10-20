def sort_stack(st):
    if len(st)==1:
        return
    tmp = st.pop()
    sort_stack(st)
    insertAtBottom(st,tmp)

def insertAtBottom(st,item):
    if len(st)==0 or item >= st[-1]:
        st.append(item)
        return 

    tmp = st.pop()
    insertAtBottom(st,item)
    st.append(tmp)
    

st = [9,5,4,3,6]
sort_stack(st)
print(st)