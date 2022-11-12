arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort()
dep.sort()
i,j,n = 1,0,len(arr)
plat_needed,minplats  = 1,1
while i<n and j<n:
    if arr[i]<=dep[j]:
        plat_needed += 1
        i += 1
    else:
        plat_needed -= 1
        j += 1
    minplats = max(plat_needed,minplats)

print(minplats)
    