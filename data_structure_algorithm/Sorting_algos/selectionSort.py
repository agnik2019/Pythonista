def selectionSort(arr):
    sortedlist = []
    for i in range(len(arr)):
        min_index = find_min_index(arr)
        print(f"{arr} and {sortedlist}")
        sortedlist.append(arr.pop(min_index))
    return sortedlist

def find_min_index(arr):
    min_idx = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx


arr = [4,2,1,88,23,1,200]
print(selectionSort(arr))