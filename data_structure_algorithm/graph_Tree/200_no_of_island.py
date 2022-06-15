class Solution(object):
    def dfs(self,grid,r,c):
        if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == '1':
            grid[r][c] = '0'
            self.dfs(grid,r+1,c)
            self.dfs(grid,r-1,c)
            self.dfs(grid,r,c-1)
            self.dfs(grid,r,c+1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    count += 1
        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
sol = Solution()
print(sol.numIslands(grid))