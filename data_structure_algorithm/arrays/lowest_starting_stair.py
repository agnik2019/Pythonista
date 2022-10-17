jumps = [1,-4,-2,3]

neg_val = 0
for j in jumps:
    if j<0:
       neg_val += j
start_pos = -neg_val+1

res = 0
is_true,flag = True, True
for i in range(start_pos,1,-1):
    res = start_pos
    for j in jumps:
        res += j
        if res <= 0:
            flag = False
            break
    if flag == False:
        break
    start_pos -= 1
print(start_pos+1)
    

