class Solution:
    def solveNQueens(self, n):
        valid_boards = []
        def check(row, banned_cols, banned_diag_sum, banned_diag_diff, board):
            if row==n:
                valid_boards.append(board)
                return
            for col in range(n):
                can_place_at_row_col = (col not in banned_cols) and \
                                       (row+col not in banned_diag_sum) and \
                                       (row-col not in banned_diag_diff)
                if can_place_at_row_col:
                    check(row+1, 
                        banned_cols.union({col}), 
                        banned_diag_sum.union({row+col}), 
                        banned_diag_diff.union({row-col}),
                        board+['.'*col+'Q'+'.'*(n-col-1)])
            return
        check(0, banned_cols=set(), banned_diag_sum=set(), banned_diag_diff=set(), board=[])
        return valid_boards
		
		