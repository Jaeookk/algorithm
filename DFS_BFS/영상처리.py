# https://level.goorm.io/exam/49077/%EC%98%81%EC%83%81%EC%B2%98%EB%A6%AC/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque


c, r = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

# def dfs(x,y):
# 	global visited, temp
# 	dx, dy = [-1,1,0,0], [0,0,-1,1]
# 	for i in range(4):
# 		nx, ny = x+dx[i], y+dy[i]
# 		if 0<=nx<r and 0<=ny<c and arr[nx][ny] == "#":
# 			if not visited[nx][ny]:
# 				visited[nx][ny] = True
# 				temp += 1
# 				dfs(nx,ny)
# 	return 1


def bfs(x, y):
    global visited, temp
    q = deque()
    q.append((x, y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if 0 <= na < r and 0 <= nb < c:
                if arr[na][nb] == "#" and not visited[na][nb]:
                    q.append((na, nb))
                    visited[na][nb] = True
                    temp += 1
    return 1


count = 0
max_size = 0
visited = [[False for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        temp = 0
        if arr[i][j] == "#" and not visited[i][j]:
            visited[i][j] = True
            temp += 1
            count += bfs(i, j)
            max_size = max(max_size, temp)
print(count)
print(max_size)
