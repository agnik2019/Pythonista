class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        visited = [[0]*col for _ in range(row)]
        distance = [[0]*col for _ in range(row)]
        queue= []
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r,c,0))
                    visited[r][c] = 1
        while queue:
            i,j,steps = queue[0][0],queue[0][1],queue[0][2]
            queue.pop(0)
            distance[i][j] = steps
            for new_i,new_j in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=new_i<row and 0<=new_j<col and visited[new_i][new_j] == 0:
                    visited[new_i][new_j] = 1
                    queue.append((new_i,new_j,steps+1))
        return distance
                    
        