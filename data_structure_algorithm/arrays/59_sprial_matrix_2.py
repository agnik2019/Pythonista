from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        if not n: return matrix
        # construct a matrix of zeros
        matrix = [[0] * n for _ in range(n)]
        top,left,bottom,right = 0,0,n-1, n-1
        num = 1
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top,bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right,left-1,-1):
                if top <= bottom:
                    matrix[bottom][i] = num
                    num += 1
            bottom -= 1
            for i in range(bottom,top-1,-1):
                if left <= right:
                    matrix[i][left] = num
                    num += 1
            left +=1
        return matrix

print(Solution().generateMatrix(3))