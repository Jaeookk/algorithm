# https://school.programmers.co.kr/learn/courses/30/lessons/17679#
def check_block(m,n,board):
    graph = [[1]*n for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j] == "": continue
            if (board[i-1][j-1] == board[i][j]
                and board[i][j-1] == board[i][j]
                and board[i-1][j] == board[i][j]):
                graph[i][j] = min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j]) + 1
    return graph

  
def remove_block(m,n,board,graph):
    cnt = []
    for i in range(1,m):
        for j in range(1,n):
            if graph[i][j] >= 2:
                board[i-1][j-1], board[i-1][j], board[i][j-1], board[i][j] = "", "", "", ""
                cnt.extend([(i-1,j-1),(i-1,j),(i,j-1),(i,j)])
    return board, len(set(cnt))

  
def fill_empty(m,n,board):
    for j in range(n):
        point = []
        for i in range(m-1,-1,-1):
            if not point:
                if board[i][j] == "":
                    point.append((i,j))
            else:
                if board[i][j] == "":
                    point.append((i,j))
                else:
                    x, y = point.pop(0)
                    board[x][y] = board[i][j] # 가장 밑에 처음 나왔던 빈칸으로 옮겨줌
                    board[i][j] = ""  # 옮기고 난 부분은 빈칸으로 변경. 이 i,j 좌표도 point에 추가해줘야 한다
                    point.append((i,j))
    return board
        
    
def solution(m, n, board):
    answer = 0
    new_board = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_board[i][j] = board[i][j]
    
    while True:
        graph = check_block(m,n,new_board)
        new_board, count = remove_block(m,n,new_board, graph)
        if count == 0: break
        new_board = fill_empty(m,n,new_board)
        answer += count
                
    return answer
