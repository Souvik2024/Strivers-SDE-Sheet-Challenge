class Solution:
    def setZeroes(self, matrix):
        row = [1]*len(matrix)
        col = [1]*len(matrix[0])
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0