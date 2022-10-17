# -3 -2 3 4 -1 -10 9 0
def seg_pos_neg(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j]<0:
            temp = arr[i]
            arr[i] = arr[j]
            i += 1
            arr[j] = temp
    return arr

arr = [-12,11,-13,-5,6,0,-7,5,-3,-6]
print(seg_pos_neg(arr))
