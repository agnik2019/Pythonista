class TicTacToe(object):
    def __init__(self,n):
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.n = n
    def move(self,row,col, player):
        self.board[row][col] = player

        matrix = self.board
        n = self.n

        def checkrow(r):
            for c in range(n):
                if matrix[r][c] != player:
                    return False
            return True
        def checkcol(c):
            for r in range(n):
                if matrix[r][c] != player:
                    return False
            return True
        def checkrow(r):
            for c in range(n):
                if matrix[r][c] != player:
                    return False
            return True

        def checkDiag():
            for d in range(n):
                if matrix[d][d] != player:
                    return False
            return True

        def checkAntiDiag():
            for r in range(n):
                if matrix[r][n-r-1] != player:
                    return False
            return True

        for r in range(n):
            if checkrow(r): return player

        for c in range(n):
            if checkcol(c): return player
        if checkDiag(): return player
        if checkAntiDiag(): return player


tictactoe = TicTacToe(3)  
tictactoe.move(0,0,1)
tictactoe.move(0,2,2)
print(tictactoe.move(2,2,1))
tictactoe.move(1,1,2)
tictactoe.move(2,0,1)
print(tictactoe.move(1,0,2))
print(tictactoe.move(2,1,1))