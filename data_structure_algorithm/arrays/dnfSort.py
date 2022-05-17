# dutch national flag
def dnfSort(arr):
    l,m,h = 0,0,len(arr)-1
    while m <= h:
        x = arr[m]
        if x == 0:
            arr[l],arr[m] = arr[m],arr[l]
            l += 1
            m += 1
        elif x == 1:
            m += 1
        else:
            arr[m],arr[h] = arr[h],arr[m]
            h -= 1

arr = [2,0,1,0,0,2,2,1]
dnfSort(arr)
print(arr)         