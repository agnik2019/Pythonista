class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(r,c,index):
            if index == len(word): return True
            if r<0 or r>= len(board) or c<0 or c>= len(board[0]) or board[r][c] != word[index]:
                return False
            temp = board[r][c]
            board[r][c] = '*'
            if dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1):
                return True
            board[r][c] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False