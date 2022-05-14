def quickSort(values):
    if len(values) <= 1:
        return values    
    pivot = values[0]
    greater_than_pivot = []
    lesser_than_pivot = []
    for value in values[1:]:
        if value <= pivot:
            lesser_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quickSort(lesser_than_pivot)+[pivot] + quickSort(greater_than_pivot)


arr = [4,2,1,88,23,1,200]
print(quickSort(arr))