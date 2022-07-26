from collections import deque

def solution(board):
    n = len(board)
    
    queue = deque()
    queue.append(({(0,0), (0,1)}, 0)) # 로봇의 좌표는 set 이용
    visited = []
    visited.append({(0,0), (0,1)})

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        position, distance = queue.popleft()
        position = list(position)
        # 마지막에 도달하면 종료
        if (n-1, n-1) in position:
            break
            
        x1, y1 = position[0]
        x2, y2 = position[1]
        
        tmp = []
        
        # 상, 하, 좌, 우 이동
        for i in range(4):
            nx1 , nx2 = position[0][0] + dx[i], position[1][0] + dx[i]
            ny1 , ny2 = position[0][1] + dy[i], position[1][1] + dy[i]
            if 0<= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                tmp.append({(nx1, ny1), (nx2, ny2)})
                # if {(nx1, ny1),(nx2, ny2)} not in visited:
                    # queue.append(({(nx1, ny1), (nx2, ny2)}, distance + 1))
                    # visited.append({(nx1, ny1), (nx2, ny2)})
        # 회전 총 8가지: 가로일때 세로로 회전 4개, 세로일때 가로로 회전 4개
        for i in [-1, 1]:
            if x1 == x2: # 가로일때
                if 0 <= x1+i < n and 0 <= x2+i < n and board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                    tmp.append({(x1, y1), (x1+i, y1)})
                    tmp.append({(x2, y2), (x2+i, y2)})
                    # queue.append(({(x1, y1), (x1+i, y1)}, distance + 1))
                    # queue.append(({(x2+i, y2), (x2, y2)}, distance + 1))
            if y1 == y2: # 세로일때
                if 0 <= y1+i < n and 0 <= y2+i < n and board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                    tmp.append({(x1, y1), (x1, y1+i)})
                    tmp.append({(x2, y2), (x2, y2+i)})
                    # queue.append(({(x1, y1), (x1, y1+i)}, distance + 1))
                    # queue.append(({(x2, y2), (x2, y2+i)}, distance + 1))
        # 모든 경우의 수를 꺼내서 이동 진행                  
        for pos in tmp:
            # 방문하지 않았을 경우 
            if pos not in visited:
                queue.append((pos, distance + 1))
                visited.append(pos)
                
    return distance
