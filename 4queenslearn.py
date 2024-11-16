def is_safe(board,col,row):
    for i in range(col):
        if board[row][i]==1:
            return False
    i,j=row,col
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=row,col
    while i<len(board) and j>=0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
    return True
def print_board(board):
    for i in board:
        for j in i:
            if j==1:
                print('Q',end='')
            else:
                print('.',end='')
        print()
def print_board_back(board):
    print("Another solution ")
    for i in zip(*board):
        for j in i:
            if j==1:
                print('Q',end='')
            else:
                print('.',end='')
        print()


def solve_csp(board,col):
    if col>=len(board):
        return True
    for i in range(len(board)):
        if is_safe(board,col,i):
            board[i][col]=1
            if solve_csp(board,col+1):
                return True
            board[i][col]=0
    return False

n=5
board=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(0)
    board.append(row)
if solve_csp(board,0):
    print("Solution found")
    print_board(board)
    print_board_back(board)
else:
    print("No solution  ")