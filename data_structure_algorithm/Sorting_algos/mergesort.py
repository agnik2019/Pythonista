# [4,2,1,88,23,1,200]

def combine(arr,s,m,e):
    temp = [0]*(e+1)
    #  s  to m
    # m+1 to e
    i = s
    j = m+1
    k = s
    while k <= e:
        temp[k] = arr[k]
        k += 1
    k = s   
    while i<= m and j<= e:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            k += 1
            i +=1
        else:
            arr[k] = temp[j]
            k += 1
            j += 1
    while i <=m :
        arr[k] = temp[i]
        k += 1
        i += 1
    while j <= e:
        arr[k] = temp[j]
        k += 1
        j += 1

    del temp

        

def mergeRecur(arr,s,e):
    if s>=e:
        return
    m = (s+e)//2
    mergeRecur(arr,s,m)
    mergeRecur(arr,m+1,e)
    combine(arr,s,m,e)


def mergeSort(arr):
    mergeRecur(arr,0,len(arr)-1)

arr = [4,2,1,88,23,1,200]
mergeSort(arr)
print(arr)