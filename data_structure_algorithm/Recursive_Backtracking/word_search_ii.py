from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:         
        rows, cols = len(board),len(board[0])
        visited = set()    
        def dfs(r,c,idx):
            if len(word) == idx:
                return True
            elif r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] != word[idx]:
                return False
            else:
                visited.add((r,c))
                result = (
                dfs(r-1,c,idx+1)or
                dfs(r+1,c,idx+1) or 
                dfs(r,c-1,idx+1) or 
                dfs(r,c+1,idx+1)
                )
                visited.remove((r,c))                  
                return result
        
        for r in range(rows):
            for c in range(cols):
                if (dfs(r,c,0)):
                    return True
        return False
            
                
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for word in words:
            if self.exist(board,word):
                res.append(word)
        return res

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
print(Solution().findWords(board,words))