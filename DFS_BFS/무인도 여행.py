# https://school.programmers.co.kr/learn/courses/30/lessons/154540?language=python3

from collections import deque

def solution(maps):
    answer = []
    visited = [[0] * (len(maps[0])) for _ in range(len(maps))]
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visited[x][y] = 1
        day = 0
        dx, dy = [1,-1,0,0], [0,0,1,-1]       
        while q:
            x,y = q.popleft()
            day += int(maps[x][y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                        visited[nx][ny] = 1
                        q.append((nx,ny))
        answer.append(day)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                bfs(i,j)
                
    if answer:
        return sorted(answer)
    else:
        return [-1]
