def NGR(nums):
    st = []
    res = [-1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        curval = nums[i]
        while st and st[-1]<= curval:
            st.pop()
        res[i] = st[-1] if st else -1
        st.append(curval)
    return res

nums = [2,4,1,3,1,6]
print(NGR(nums))