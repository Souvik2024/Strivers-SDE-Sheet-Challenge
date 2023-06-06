class Solution:
    def rotate(self, matrix):
        ROW, COL = len(matrix), len(matrix[0])
        for r in range(ROW):
            for c in range(r, COL):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in range(ROW):
            l, r = 0, COL-1
            while l < r:
                matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
                l, r = l+1, r-1