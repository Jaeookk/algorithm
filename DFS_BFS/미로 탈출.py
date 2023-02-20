# https://school.programmers.co.kr/learn/courses/30/lessons/159993
from collections import deque


def solution(maps):
    pos = [-1,-1,0]
    flag = False
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # find start
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                pos = [i, j, 0]
    #find lever
    queue = deque([pos])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[pos[0]][pos[1]] = 1

    while queue:
        temp = queue.popleft()
        if maps[temp[0]][temp[1]] == "L":
            pos = temp
            flag = True
            break
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    queue.append([nx, ny, temp[2] + 1])
                    visited[nx][ny] = 1
    if flag == False:
        return -1

    #find exit
    queue = deque([pos])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[pos[0]][pos[1]] = 1

    while queue:
        temp = queue.popleft()
        if maps[temp[0]][temp[1]] == "E":
            return temp[2]
            break
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    queue.append([nx, ny, temp[2] + 1])
                    visited[nx][ny] = 1
    return -1
