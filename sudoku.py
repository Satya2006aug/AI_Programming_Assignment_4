# Problem 3: Sudoku using CSP

grid = [
[0,0,3,0,2,0,6,0,0],
[9,0,0,3,0,5,0,0,1],
[0,0,1,8,0,6,4,0,0],
[0,0,8,1,0,2,9,0,0],
[7,0,0,0,0,0,0,0,8],
[0,0,6,7,0,8,2,0,0],
[0,0,2,6,0,9,5,0,0],
[8,0,0,2,0,3,0,0,9],
[0,0,5,0,1,0,3,0,0]
]


def is_valid(board,row,col,num):

    # row check
    for i in range(9):
        if board[row][i] == num:
            return False

    # column check
    for i in range(9):
        if board[i][col] == num:
            return False

    # 3x3 box check
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True


def solve(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                for num in range(1,10):

                    if is_valid(board,row,col,num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


solve(grid)

print("\nSudoku Solution:\n")

for row in grid:
    print(row)
