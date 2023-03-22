# https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque


def solution(board):
    answer = 0
    r = len(board)
    c = len(board[0])
    q = deque()
    visited = []
    count = [[10000] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                q.append((i, j))
                visited.append((i, j))
                count[i][j] = 0
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        if board[x][y] == "G":
            answer = count[x][y]
            break
        idx = 0
        nx, ny = x, y
        while idx < 4:
            temp = (nx, ny)
            nx += dx[idx]
            ny += dy[idx]
            if nx < 0 or r <= nx or ny < 0 or c <= ny or board[nx][ny] == "D":
                if temp not in visited:
                    visited.append(temp)
                    q.append(temp)
                    count[temp[0]][temp[1]] = min(count[x][y] + 1, count[temp[0]][temp[1]])
                idx += 1
                nx, ny = x, y

    return answer if answer > 0 else -1
