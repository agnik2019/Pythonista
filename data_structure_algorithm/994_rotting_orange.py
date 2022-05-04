class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        row_idx = [0,0,1,-1]
        col_idx = [1,-1,0,0]
        r = len(grid)
        c = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        ans = 0
        while(len(queue) != 0):
            x = queue.pop(0)
            row,col,depth = x[0],x[1],x[2]
            ans = max(ans,depth)
            for i in range(4):
                new_row = row + row_idx[i]
                new_col = col + col_idx[i]
                if new_row>=0 and new_col>= 0 and new_row<r and new_col < c and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col,depth+1))
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
            
        return ans
                
                    
        