from itertools import combinations
import sys

f = sys.stdin.readline
n, m = map(int, f().split())

graph = []
temp = [[0] * m for _ in range(n)]
for _ in range(n):
    a = list(map(int, f().split()))
    graph.append(a)

data = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            data.append((i, j))
combination = list(combinations(data, 3))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    # 4가지 방향에 대하여
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def check_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs():
    result = -1

    for datas in combination:
        for x in range(n):
            for y in range(m):
                temp[x][y] = graph[x][y]
        for i, j in datas:
            temp[i][j] = 1

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, check_score())

    return result

print(dfs())
            
