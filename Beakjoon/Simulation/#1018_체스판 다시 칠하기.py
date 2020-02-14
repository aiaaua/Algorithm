N, M = map(int, input().split())
answer = 64
board = [list(input()) for _ in range(N)]
cases = [[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4,
         [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4]

def split_board(board) : 
    boards = []
    for i in range(N-7) :
        for j in range(M-7) : 
            boards.append([board[i][j:j+8] for i in range(i, i+8)])
    return boards

for board in split_board(board) :
    for case in cases : 
        temp = 0
        for i in range(8) :
            for j in range(8) :
                if board[i][j] != case[i][j] :
                    temp += 1
        answer = min(answer, temp)
        
print(answer)
