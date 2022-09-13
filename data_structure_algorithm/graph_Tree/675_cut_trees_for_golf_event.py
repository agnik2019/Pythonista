from typing import List
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        R,C = len(forest),len(forest[0])
        trees = [(forest[i][j],i,j) for i in range(R) for j in range(C) if forest[i][j] > 1]
        trees = sorted(trees)
        print(trees)
        def bfs(sr,sc,dr,dc):
            queue = deque([(sr,sc,0)])
            seen = set((sr,sc))
            while queue:
                r,c,d = queue.popleft()
                if r== dr and c == dc: return d
                for nr,nc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                    if (0<=nr<R and 0<=nc<C and (nr,nc) not in seen and forest[nr][nc]):
                        seen.add((nr,nc))
                        queue.append((nr,nc,d+1))
            return -1
        
        sr,sc,total = 0,0,0
        for tree in trees:
            d = bfs(sr,sc,tree[1],tree[2])
            if d < 0: return -1
            total += d
            sr = tree[1]
            sc = tree[2]            
            
        return total
                        
                
            
        