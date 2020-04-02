def isSafe (board, row, col):
    # check left row
    for y in range(col):
        if board[row][y] == 1:
            return False
    # check diagonal left top
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    # check diagonal left bottom
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def generateSolution(board, col):
    # terminating condition
    # all columns covered
    global N
    if col >= N:
        return True
    # loop over all the rows
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            # recursively place other queens
            print(board)
            if generateSolution(board, col + 1):
                return True
            # unmark queen spot
            board[i][col] = 0
            
    # backtrack
    return False


N = int(input())
startCol = 0
board = [[0 for i in range(N)] for j in range(N)]

if not generateSolution(board, startCol):
    print("No Solution Exists")
else:
    print("Solution exists")
    print(board)
'''
output:
[[0, 0, 1, 0],
 [1, 0, 0, 0],
 [0, 0, 0, 1],
 [0, 1, 0, 0]]
'''
