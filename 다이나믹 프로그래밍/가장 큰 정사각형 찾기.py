# https://school.programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    r = len(board)
    c = len(board[0])
    ans = 0
    
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 :
                ans = max(ans, board[i][j])
                continue
            if board[i][j] == 1:
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
                ans = max(ans, board[i][j])
                

    return ans**2
