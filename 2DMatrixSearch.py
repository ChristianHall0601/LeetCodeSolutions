class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == target:
                    return True
        return False
