class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i,j = 0,len(matrix[0])-1
        while i<len(matrix) and j >=0:
            if target == matrix[i][j]:
                return True
            elif matrix[i][j]>target:
                j -= 1
            elif matrix[i][j]<target:
                i+=1
        return False