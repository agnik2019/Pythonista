from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        r,c = len(grid),len(grid[0])
        q,seen = deque(),set()
        q.append([0,0,k,0]) #row,col,k,steps
        seen.add((0,0,k))
        while q:
            i,j,k,s = q.popleft()
            if (i,j)==(r-1,c-1): return s
            for i1,j1 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=i1<r and 0<=j1<c and k>= grid[i][j]:
                    step = (i1,j1,k-grid[i][j],s+1)
                    if step[0:3] not in seen:
                        q.append(step)
                        seen.add(step[0:3])
        return -1
