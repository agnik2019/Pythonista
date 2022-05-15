from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        board.reverse()
        def num_to_pos(num):
            r,c = (num-1)//n,(num-1)%n
            if r %2 == 1:
                c = n - c -1 
            return [r,c]
        q = deque()
        visited = set()
        q.append([1,0])
        while q:
            squares, moves = q.popleft()
            for i in range(1,7):
                nextsquare = squares+i
                r,c = num_to_pos(nextsquare)
                if board[r][c] != -1:
                    nextsquare = board[r][c]
                if nextsquare == n*n:
                    return moves+1
                if nextsquare not in visited:
                    visited.add(nextsquare)
                    q.append([nextsquare,moves+1])
        return -1
                    
                    
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
sol = Solution()
print(sol.snakesAndLadders(board))