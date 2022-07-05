def find_path(arr,n):
    res = []
    def allPaths(row,col,ans):
        if row<0 or row >= n or col <0 or col >= n or arr[row][col]== 0:
            return
        if row == n-1 and col == n-1:
            res.append(ans)
            return
        arr[row][col] = 0
        allPaths(row+1,col,ans+'D')
        allPaths(row,col-1,ans+'L')
        allPaths(row,col+1,ans+'R')
        allPaths(row-1,col,ans+'U')
        arr[row][col] = 1
        return
    allPaths(0,0,"")
    return res

arr = [[1,0,0],
        [1,1,0],
        [1,1,1]]
print(find_path(arr,len(arr)))
