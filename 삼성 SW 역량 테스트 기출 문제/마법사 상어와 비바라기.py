# BOJ 21610
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

q = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

for _ in range(m):
    idx, distance = map(int, input().split())
    dx = direction[idx - 1][0] * distance
    dy = direction[idx - 1][1] * distance

    cloud = [[0] * n for _ in range(n)]

    # 1번
    while q:
        x, y = q.popleft()
        new_x = (x + dx) % n
        new_y = (y + dy) % n
        cloud[new_x][new_y] = 1

    # 2번
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                board[i][j] += 1

    # 4번
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                cnt = 0
                for k in [1, 3, 5, 7]:
                    nx, ny = i + direction[k][0], j + direction[k][1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] > 0:
                            cnt += 1
                board[i][j] += cnt

    # 5번
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and cloud[i][j] != 1:
                board[i][j] -= 2
                q.append((i, j))
result = 0
for i in range(n):
    for j in range(n):
        result += board[i][j]

print(result)
