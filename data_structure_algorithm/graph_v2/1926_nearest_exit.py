class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze),len(maze[0])
        queue = deque([[entrance[0],entrance[1],0]])
        maze[entrance[0]][entrance[1]] = '+' # marking as visited
        while queue:
            x,y,steps = queue.popleft()
            if (0 in [x,y] or x == m-1 or y == n-1) and [x,y] != entrance:
                return steps
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=nx<m and 0<=ny<n and maze[nx][ny] == '.':
                    maze[nx][ny] = "+"
                    queue.append([nx,ny,steps+1])
        return -1
        