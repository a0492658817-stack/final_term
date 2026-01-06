def INPUT():
    board=[]
    while(True):
        try:
            line=input().split()
            board.append([int(i) for i in line])
        except EOFError:
            break
    return board
def is_safe(board,r,c,num):
    for i in range(4):
        if(board[r][i]==num):
            return False
    for j in range(4):
        if(board[j][c]==num):
            return False
    block_row=(r//2)*2
    block_column=(c//2)*2
    for i in range(block_row,block_row+2):
        for j in range(block_column,block_column+2):
            if(board[i][j]==num):
                return False
    return True
def solve(board):
    for r in range(4):
        for c in range(4):
            if(board[r][c] == 0):
                for num in range(1,5):
                    if(is_safe(board,r,c,num)):
                        board[r][c]=num
                        if(solve(board)):
                            return True
                        board[r][c]=0
                return False
    return True            
def main():
    board=INPUT()
    solve(board)
    for row in board:
        print(*row)
main()