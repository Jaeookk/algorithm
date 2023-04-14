# https://level.goorm.io/exam/159666/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%A8%BC%EB%8D%B0%EC%9D%B4-%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
graph = [[0 for _ in range(n)] for _ in range(n)]


def dfs(x, y, depth):
    graph[x][y] += 1
    if depth == 1:
        return
    dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            dfs(nx, ny, depth + 1)


for r, c in arr:
    dfs(r - 1, c - 1, 0)

print(sum([sum(graph[i]) for i in range(n)]))
