class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        R,C = len(grid),len(grid[0])
        def posToVal(r,c):
            return r*C+c
        def valToPos(val):
            return [val // C,val % C]
        res = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                newVal = (posToVal(r,c)+k)%(R*C)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
        return res