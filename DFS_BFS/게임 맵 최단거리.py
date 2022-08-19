from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    queue = deque()
    queue.append((0,0))
    result = 0
    while queue:
        x,y = queue.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y]+1

    answer = maps[n - 1][m - 1]
    if answer == 1: return -1
    else: return answer
