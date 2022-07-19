from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0: return res
        top,left,bottom,right = 0,0,len(matrix)-1, len(matrix[0])-1
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            for i in range(right,left-1,-1):
                if top <= bottom:
                    res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom,top-1,-1):
                if left <= right:
                    res.append(matrix[i][left])
            left +=1
        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(Solution().spiralOrder(matrix))