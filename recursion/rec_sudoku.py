def solveSudoku(board) -> None:
    def isGood(num,row,col):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3
            if board[box_row][box_col] == num:
                return False
        return True
    
    def solve():
        for i in range(9):  
            for j in range(9):
                if board[i][j] == ".":
                    for x in range(1,10):
                        if isGood(str(x),i,j):
                            board[i][j] = str(x)
                            if solve():
                                return True
                            else:
                                board[i][j] = "."
                    return False   
        return True
    solve()
    print(board)
solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) 