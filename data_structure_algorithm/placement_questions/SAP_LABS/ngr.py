# next greater element right
# ip: [ 4 , 5 , 2 , 25 ]
# op: [ 5 , 25, 25 ,-1 ]
nums = [4,5,2,25]
st = []
res = [-1]*len(nums)
for i in range(len(nums)-1,-1,-1):
    while st and st[-1]<= nums[i]:
        st.pop()
    res[i] = st[-1] if st else -1
    st.append(nums[i])
    
print(res)



# REMEBER:

# NEXT GREATER RIGHT : ITERATE FROM RIGHT
# STACK TOP <= NUM (ARRAY ELEMENT)
